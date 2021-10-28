from django.contrib.auth.models import User
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



#One on One mode Modele
class UnContreUn(models.Model):
    user1     = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    user2     = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    is_accept = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user1.username } & {self.user2.username} --- {self.timestamp.date()}"


#Score of the one-on-one mode
class ScoreTwo(models.Model):
    user1   = models.ForeignKey(User, related_name="score1", on_delete=models.CASCADE)
    user2   = models.ForeignKey(User, related_name="score2",  on_delete=models.CASCADE)
    points1 = models.IntegerField()
    points2 = models.IntegerField()
    date    = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.user1.username } a {self.points1} -- {self.user2.username } a {self.points2}"


