#Importons les modules nécessaires
from django import forms
from django.contrib.auth.models import User

"""
    Créons le formulaire de connexion
"""
class ConnexionForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=50, widget=forms.TextInput(attrs={'type':'text', 'class':'form-control form-control-user', 'id':'exampleInputEmail', 'aria-describedby':'emailHelp', 'placeholder':'Saisissez votre email...'}))   
    password = forms.CharField(label="Mot-de-passe", widget=forms.PasswordInput(attrs={'type':'password', 'class':'form-control form-control-user', 'id':'exampleInputPassword',  'placeholder':'Saisissez votre mot-de-passe...'}))


"""
    Créons le formulaire d'inscription
"""
class InscriptionForm(forms.Form):
    # first_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'type': 'exampleFirstName', 'placeholder': 'First Name'}))
    # last_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'type': 'exampleFirstName', 'placeholder': 'Last Name'}))
    username = forms.CharField(label="Identifiant", max_length=50, widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'type': 'exampleFirstName', 'placeholder': 'Saisissez votre identifiant...'}))
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'type':'text', 'class':'form-control form-control-user', 'id':'exampleInputEmail', 'aria-describedby':'emailHelp', 'placeholder':'Saisissez votre email...'}))   
    password = forms.CharField(label="Mot-de-passe", widget=forms.TextInput(attrs={'type':'password', 'class':'form-control form-control-user', 'id':'exampleInputPassword',  'placeholder':'Saisissez votre mot-de-passe...'}))


