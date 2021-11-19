# serializers.py
from rest_framework import serializers

from .models import *





#serialize model Mots
class MotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mots
        fields = ('id','mot', 'indice_1', 'indice_2', 'indice_3', 'theme', 'difficulte', 'utilisateur')




# Serialize model Score
class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('id','username', 'points', 'date')




# Serialize model Feedback
class FeedbackSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id','feedback',  'date')


# Serialize model Score un contre un pour les invitations
class UnContreUnSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnContreUn
        fields = ('id','user1', 'user2', 'is_accept', 'timestamp')


# Serialize model Score un contre un avec les points
class ScoreTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoreTwo
        fields = ('id','user1', 'user2', 'points1', 'points2', 'date')