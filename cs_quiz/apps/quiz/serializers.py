from rest_framework import serializers
from cs_quiz.apps.quiz.models import Answer, Quiz


class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
    
        
class QuizRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'
        

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        exclude = ['created_at', 'updated_at']

