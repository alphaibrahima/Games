# serializers.py
from rest_framework import serializers

from .models import *



#serialize model Quiz
class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('name', 'topic', 'number_of_questions', 'time', 'required_score_to_pass', 'difficulty', )





# Serialize model Question 
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('text', 'quiz', 'created')




# Serialize model Answer 
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('text', 'correct', 'question',  'created', )



# Serialize model Answer 
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('quiz', 'user', 'score')

