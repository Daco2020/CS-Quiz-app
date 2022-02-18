from rest_framework import viewsets, generics
from cs_quiz.apps.quiz.models import Answer, Quiz
from cs_quiz.apps.quiz.serializers import AnswerCreateSerializer, AnswerListSerializer, QuizListSerializer, QuizRetrieveSerializer


# 쿼리파람에 맞게 리스트를 반환하려면?
class QuizListView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizListSerializer


# 해당 퀴즈의 '답변 수'도 함께 반환하려면?
class QuizRetrieveView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizRetrieveSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerCreateSerializer
    

# 해당되는 퀴즈의 답변만 반환하려면?
class AnswerListView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer