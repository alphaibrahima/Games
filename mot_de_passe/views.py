from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


from .models import Feedback, Mots, Score, UnContreUn
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PropositionForm


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
    scores = Score.objects.all().order_by('-points')
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





def Invit(request, id):
    userId = User.objects.get(id = id)
    print(userId)
    connected_user = request.user
    print(connected_user)

    UnContreUn.objects.create(user1 = connected_user, user2 = userId)
    messages.add_message(request, messages.SUCCESS, f" Patientez que  {userId} accepte l'invitation ")
    return redirect('1vs1')

    # return render(request, 'invite.html', locals())


def ShowInvi(request):
    invits = UnContreUn.objects.filter(is_accept = False, user2 = request.user)
    return render(request, 'invite.html', locals())


def AccpetInv(request, id):
    mode = UnContreUn.objects.get(id = id)
    print(mode)

    if mode.is_accept == False:
        mode.is_accept = True
        mode.save()
        messages.add_message(request, messages.SUCCESS, f" Que le meilleur gagne ")
    return redirect('1vs1')





def modeOne(request):
    users = User.objects.all()
    return render(request, 'modeUn.html', locals())


def jeu1vs1(request):
    liste_mots = list(Mots.objects.all().values())
    themes = list(Mots.objects.order_by().values_list('theme', flat=True).distinct())
    difficultes = list(Mots.objects.order_by().values_list('difficulte', flat=True).distinct())
    return render(request, 'jeu1vs1.html', locals())





