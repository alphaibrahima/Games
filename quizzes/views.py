from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Question, Answer, Result
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class QuizListView(LoginRequiredMixin, ListView,):
    login_url = 'connexion'
    model = Quiz
    template_name = 'quizes/main.html'

@login_required
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quizes/quiz.html', {'obj': quiz})

@login_required
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': quiz.time,
    })

@login_required
def save_quiz_view(request, pk):
    #print(request.POST)
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
 
        data_.pop('csrfmiddlewaretoken')
        print(type(data_))


        for k in data_.keys():
            print('key : ',k)
            question= Question.objects.get(text=k)
            questions.append(question)
        print(questions)

        user=request.user
        quiz = Quiz.objects.get(pk=pk)

        score=0
        multiplier =100
        results =[]
        correct_answer = None

        for q in questions:
            a_selected=request.POST.get(q.text)
            if a_selected != "":
                question_answers= Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score+=1/len(questions)
                            print(a.text,' - ',a_selected,' s:',score)
                            correct_answer=a.text
                    else:
                        if a.correct:
                            correct_answer=a.text
                results.append({str(q) : {'correct_answer': correct_answer , 'answered': a_selected}})
            else:
                results.append({str(q) : 'not answered'})
        score_=score*multiplier; 
        
        Result.objects.create(quiz=quiz,user=user,score=score_)  
        if score_ >= quiz.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_ ,'results':results })
        else:
            return JsonResponse({'passed': False,'results':results, 'score': score_ })
