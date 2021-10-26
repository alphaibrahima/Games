#Importons les modules nécessaires
from django.urls import path
from accueil import views

#Définissons les routes vers nos vues
urlpatterns = [
    path('connexion/', views.connexion, name = "connexion"),
    path('inscription/', views.inscription, name = "inscription"),
    path('', views.accueil, name = "accueil"),
    path('deconnexion/', views.deconnexion, name = "deconnexion"),


]