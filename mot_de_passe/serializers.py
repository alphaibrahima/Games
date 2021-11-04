# serializers.py
from rest_framework import serializers

from .models import *






class MotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mots
        fields = ('mot', 'indice_1', 'indice_2', 'indice_3', 'theme', 'difficulte', 'utilisateur')