from rest_framework import serializers
from cs_quiz.apps.quiz.models import Answer, Quiz


class QuizListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.content')
    tag = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Quiz
        fields = '__all__'
    
        
class QuizRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.content')
    tag = serializers.StringRelatedField(many=True)
    answer_count = serializers.SerializerMethodField(method_name='sum_answer')
    
    class Meta:
        model = Quiz
        fields = ['id', 'category', 'tag', 'content', 'level', 'answer_count']
        
    def sum_answer(self, id):
        answer_list = Answer.objects.filter(quiz=id)
        return len(answer_list)
    
    
class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerListSerializer(serializers.Serializer):
    quiz = serializers.CharField(source='quiz.content')
    count = serializers.IntegerField()
    answers = serializers.ListField()

