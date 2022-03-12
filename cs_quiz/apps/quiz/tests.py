import json
from django.urls import reverse
from rest_framework.test import APITestCase
from cs_quiz.apps.quiz.models import *
from cs_quiz.apps.quiz.serializers import *
from django.test import TestCase

class QuizViewTestCase(APITestCase):
    url = reverse('cs_quiz.apps.quiz:quiz-list')
    
    def setUp(self):
        self.category = Category.objects.create(content='네트워크', depth=0)
        self.tag = Tag.objects.create(content='http')
        self.quiz = Quiz.objects.create(category=self.category, content='퀴즈테스트', level=0)
        self.quiztag = QuizTag.objects.create(quiz=self.quiz, tag=self.tag)

    def test_quiz_list_view(self):
        res = self.client.get(self.url)
        self.assertEqual(200, res.status_code)

        quiz_serializer_data = QuizListSerializer(instance=self.quiz).data
        res_data = json.loads(res.content)
        
        self.assertEqual([quiz_serializer_data], res_data)