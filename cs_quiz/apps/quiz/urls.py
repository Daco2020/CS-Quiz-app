from django.urls import path, include
from rest_framework import routers
from .views import AnswerCreateView, AnswerListView, QuizListView, QuizRetrieveView

# router = routers.DefaultRouter()
# router.register(r"answer", AnswerCreateView)
app_name = 'cs_quiz.apps.quiz'

urlpatterns = [
    path("", QuizListView.as_view(), name="quiz-list"),
    path("<int:pk>/", QuizRetrieveView.as_view(), name="quiz-retrieve"),
    path("answers/", AnswerCreateView.as_view(), name="answer-create"),
    path("<int:pk>/answers/", AnswerListView.as_view(), name="answer-list"),
]