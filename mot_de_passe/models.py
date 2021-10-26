from django.db import models
import datetime


# Create your models here.
class Mots(models.Model):
    __tablename__ = 'mots'

    mot = models.CharField(max_length=100)
    indice_1 = models.CharField(max_length=100)
    indice_2 = models.CharField(max_length=100)
    indice_3 = models.CharField(max_length=100)
    theme = models.CharField(max_length=100, null=True)
    difficulte = models.CharField(max_length=100, null=True)
    utilisateur = models.CharField(max_length=100, null=True)

    # city = models.CharField(max_length=45, blank=True, null=True)
    # country = models.CharField(max_length=45, blank=True, null=True)
    # intitule = models.CharField(max_length=100, blank=True, null=True)
    # price = models.IntegerField(blank=True, null=True)
    # monnaie = models.CharField(max_length=45, blank=True, null=True)
    # seller = models.CharField(max_length=45, blank=True, null=True)
    # date = models.CharField(max_length=45, blank=True, null=True)
    # surface = models.IntegerField(blank=True, null=True)
    # chambre = models.IntegerField(blank=True, null=True)

class Score(models.Model):
    username = models.CharField(max_length=100)
    points = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.now)


class Feedback(models.Model):
    feedback = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.datetime.now)