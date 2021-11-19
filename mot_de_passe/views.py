from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.base import View
from django.http import HttpResponse



from .models import Feedback, Mots, Score, UnContreUn, ScoreTwo
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from .forms import PropositionForm

#API
from rest_framework import viewsets
from .serializers import ( MotsSerializer, ScoreSerializer, FeedbackSerializer,
                           UnContreUnSerializer, ScoreTwoSerializer
                        )


# Create your views here.
# @login_required
def mot_de_passe(request):
    liste_mots = list(Mots.objects.all().values())
    themes = list(Mots.objects.order_by().values_list('theme', flat=True).distinct())
    difficultes = list(Mots.objects.order_by().values_list('difficulte', flat=True).distinct())
    # print(difficultes)
    # print(list(liste_mots)[0]['id'])
    return render(request, 'index.html', locals())



# @login_required
def scores_view(request):
    user = request.user
    # print(user.id)
    userId = Score.objects.filter(username = user).order_by('-date')
    scores = Score.objects.all().order_by('-points')
    scoreb = scores.order_by('username').distinct('username')
    scoresauth = Score.objects.all().order_by('username').distinct('username')
    
    # print(list(liste_mots)[0]['id'])
    return render(request, 'score.html', locals())



@csrf_exempt
def score_update(request):
    if request.method == 'POST':
        new_score = Score(username = request.POST['Joueur'], points=request.POST['Score'])
        new_score.save()

        # if 'Score' in request.POST:
        #     # pieFact = request.POST['pieFact']
        #     print(request.POST['Joueur'])
            # print(user)

        return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')



@csrf_exempt
def add_feedback(request):
    if request.method == 'POST':
        Feedback.objects.create(feedback = request.POST['Feedback'])
        # new_score.save()

        # if 'Score' in request.POST:
        #     # pieFact = request.POST['pieFact']
        #     print(request.POST['Joueur'])
            # print(user)

        return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpResponse('FAIL!!!!!')


"""
    Créons la vue pour le formulaire d'Inscription
"""
# @login_required
def proposition(request):
    #Chargeaons le formulaire d'inscription
    form = PropositionForm(request.POST)
    # print(form.is_valid())
    if form.is_valid():
        mdp = form.cleaned_data["mdp"]
        indice_1 = form.cleaned_data["indice_1"]
        indice_2 = form.cleaned_data["indice_2"]
        indice_3 = form.cleaned_data["indice_3"]
        theme = form.cleaned_data["theme"]
        difficulte = form.cleaned_data["difficulte"]
        print(mdp)
        #Insérons un nouvel utilisateur dans la BDD à l'aide de la méthode create_user
        Mots.objects.create(mot = mdp, indice_1 = indice_1, indice_2 = indice_2, indice_3 = indice_3, theme = theme, difficulte = difficulte, utilisateur = request.user)
         
        # Chargeons les mots de la BDD
        liste_mots = list(Mots.objects.all().values())

        return redirect('mot_de_passe')
    else:
        form = PropositionForm()

        return render(request, 'proposition_mdp.html', locals())






# la page ou inviter les autres utilisateurs 
def modeOne(request):
    users = User.objects.all()
    return render(request, 'modeUn.html', locals())



# creation de l'invitation
def Invit(request, id):
    userId = User.objects.get(id = id)
    # userId = get_object_or_404(UnContreUn, id=id)
    print(userId)
    connected_user = request.user
    print(connected_user)

    modeUn = UnContreUn.objects.create(user1 = connected_user, user2 = userId)
    modeUn.save()
    messages.add_message(request, messages.SUCCESS, f" Patientez que  {userId} accepte l'invitation ")
    # return redirect('mot_de_passe')
    return redirect('/mdp/sale/%d/'%modeUn.id)

    # return render(request, 'invite.html', locals())


# affichage des invitations
def ShowInvi(request):
    invits = UnContreUn.objects.filter(is_accept = False, user2 = request.user)
    return render(request, 'invite.html', locals())


#traitement de l'invitation 
def AccpetInv(request, id):
    # mode = UnContreUn.objects.get(id = id)
    mode = get_object_or_404(UnContreUn, pk=id)
    print("#############################")
    print(mode)

    if mode.is_accept == False:
        mode.is_accept = True
        mode.save()
        messages.add_message(request, messages.SUCCESS, f" Que le meilleur gagne ")
        return redirect('/mdp/sale/%d/'%id)
    # return redirect('jeu1Sall')
    # return redirect('mot_de_passe')
    return render(request, 'invite.html', locals())



def Salon(request, id):
    modeun = UnContreUn.objects.filter(id=id, is_accept = True)
    liste_mots = list(Mots.objects.all().values())
    themes = list(Mots.objects.order_by().values_list('theme', flat=True).distinct())
    difficultes = list(Mots.objects.order_by().values_list('difficulte', flat=True).distinct())

    if request.is_ajax():
        liste_mots = list(Mots.objects.all().values())
        themes = list(Mots.objects.order_by().values_list('theme', flat=True).distinct())
        difficultes = list(Mots.objects.order_by().values_list('difficulte', flat=True).distinct())
        # maths = UnContreUn.objects.all()
        maths = list(UnContreUn.objects. filter(id=id).values())
           
        return JsonResponse({
            'mots'   :liste_mots,
            'themes' :themes,
            'diff'   : difficultes,
            'equipe' : maths,
            }, status=200)
    return render(request, 'jeu1vs1.html', locals())




# for display count of notifications 
def CountNotifications(request):
    count_notifications = None
    if request.user.is_authenticated:
        count_notifications =  UnContreUn.objects.filter(is_accept = False, user2 = request.user).count()
    return {'count_notifications': count_notifications}



# class jeu1Sall(View):
#     def get(self, request, id):
        
#         if request.is_ajax():
#             liste_mots = list(Mots.objects.all().values())
#             themes = list(Mots.objects.order_by().values_list('theme', flat=True).distinct())
#             difficultes = list(Mots.objects.order_by().values_list('difficulte', flat=True).distinct())
#             # maths = UnContreUn.objects.all()
#             maths = list(UnContreUn.objects. filter(id=id).values())
           
#             return JsonResponse({
#                 'mots'   :liste_mots,
#                 'themes' :themes,
#                 'diff'   : difficultes,
#                 'equipe' : maths,
#                 }, status=200)
                
#         return render(request, 'jeu1vs1.html')













# conf API Model Mots
class MotsViewSet(viewsets.ModelViewSet):
    queryset = Mots.objects.all().order_by('theme')
    serializer_class = MotsSerializer


# conf API Model Score
class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all().order_by('-date')
    serializer_class = ScoreSerializer


# conf API Model Feedback
class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all().order_by('-date')
    serializer_class = FeedbackSerializer


# conf API Model UncontreUn
class ContreUnViewSet(viewsets.ModelViewSet):
    queryset = UnContreUn.objects.all().order_by('timestamp')
    serializer_class = UnContreUnSerializer



# API Model scoreTwo pour le score un contre un
class ScoreTwoViewSet(viewsets.ModelViewSet):
    queryset = ScoreTwo.objects.all().order_by('date')
    serializer_class = ScoreTwoSerializer


