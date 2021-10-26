#Importons les modules nécessaires
from django.shortcuts import render, redirect
from .forms import ConnexionForm, InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


"""
    Créons la vue d'accueil, à partir d'où nous pourrons accéder aux visualisations
"""
# @login_required
def accueil(request):
    return render(request, 'accueil.html')

"""
    Créons la vue pour le formulaire de connexion
"""
def connexion(request):
    #Chargeaons le formulaire de connexion
    form = ConnexionForm(request.POST)
    print()
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        print(username)
        #Testons la connexion avec les informations de l'utilisateur
        user = authenticate(username = username, password = password)
        if user : 
            login(request, user)
            return render(request, 'accueil.html', locals())
        else:
            error = True
            return render(request, 'connexion.html', locals())
    else:
        form = ConnexionForm()

        return render(request, 'connexion.html', locals())

"""
    Créons la vue pour le formulaire d'Inscription
"""
def inscription(request):
    #Chargeaons le formulaire d'inscription
    form = InscriptionForm(request.POST)
    print(form.is_valid())
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        # first_name = form.cleaned_data["first_name"]
        # last_name = form.cleaned_data["last_name"]
        email = form.cleaned_data["email"]
        print(email)


        #Insérons un nouvel utilisateur dans la BDD à l'aide de la méthode create_user
        user = User.objects.create_user(username = username, email = email, password = password)
         
        # user.first_name, user.last_name = first_name, last_name
        # user.save()

        #Authentifions le nouvel utilisateur
        user = authenticate(username = username, password = password)
        login(request, user)

        return render(request, 'accueil.html', locals())
    else:
        form = InscriptionForm()

        return render(request, 'inscription.html', locals())

@login_required
def deconnexion(request):
    logout(request)

    return redirect('connexion')

