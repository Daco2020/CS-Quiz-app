import random
from rest_framework.response import Response
from rest_framework import viewsets, generics, views
from cs_quiz.apps.quiz.models import Answer, Category, Quiz
from cs_quiz.apps.quiz.serializers import AnswerCreateSerializer, AnswerListSerializer, QuizListSerializer, QuizRetrieveSerializer


class QuizListView(generics.ListAPIView):
    serializer_class = QuizListSerializer
    
    def get_queryset(self):
        category = self.request.query_params.get('category')
        level = self.request.query_params.get('level')
        
        if category and level :
            queryset = Quiz.objects.filter(category=category, level=level)
        elif not category and not level :
            queryset = Quiz.objects.all()
        elif not category :
            queryset = Quiz.objects.filter(level=level)
        elif not level :
            queryset = Quiz.objects.filter(category=category)
        
        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:3]


class QuizRetrieveView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizRetrieveSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    

class AnswerListView(views.APIView):
    def get(self, request, pk):
        answer_list = Answer.objects.filter(quiz=pk)
        count = len(answer_list)
        
        data = {
            'quiz' : answer_list[0].quiz,
            'count' : count,
            'answers' : [{
                'id' : answer.id,
                'content' : answer.content,
                'correct_point' : answer.correct_point,
                'reference_url' : answer.reference_url,
            } for answer in answer_list],
        } 
        serializer = AnswerListSerializer(instance=data)
        
        return Response(serializer.data)