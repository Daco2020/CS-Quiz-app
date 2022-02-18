from rest_framework.response import Response
from rest_framework import viewsets, generics, views
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
    

# 해당되는 퀴즈의 답변만 반환하려면? ok
# 퀴즈id가 아닌 퀴즈 제목을 반환하려면? ok
class AnswerListView(views.APIView):
    def get(self, request, pk):
        answer_list = Answer.objects.filter(quiz=pk)
        data = {
            'answers' : [{
                'content' : answer.content,
                'correct_point' : answer.correct_point,
                'reference_url' : answer.reference_url,
            } for answer in answer_list],
            'quiz' : answer_list[0].quiz,
        } 
        serializer = AnswerListSerializer(instance=data)
        
        return Response(serializer.data)