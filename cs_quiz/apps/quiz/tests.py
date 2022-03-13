import json
from django.urls import reverse
from rest_framework.test import APITestCase
from cs_quiz.apps.quiz.models import *
from cs_quiz.apps.quiz.serializers import *
from django.test import TestCase


class QuizViewTestCase(APITestCase):
    url = reverse('cs_quiz.apps.quiz:quiz-list') # 인자 중 args는 패스파라미터
    
    def setUp(self):
        self.category = Category.objects.create(content='네트워크', depth=0)
        self.tag = Tag.objects.create(content='http')
        self.quiz = Quiz.objects.create(category=self.category, content='퀴즈테스트', level=0)
        self.quiztag = QuizTag.objects.create(quiz=self.quiz, tag=self.tag)
        
    def test_quiz_list_view(self):
        res = self.client.get(self.url)
        self.assertEqual(200, res.status_code)

        serializer_data = QuizListSerializer(instance=self.quiz).data
        res_data = json.loads(res.content)
        self.assertEqual([serializer_data], res_data)

    def test_quiz_retrieve_view(self):
        res = self.client.get(path=f"/quiz/{self.quiz.id}/")
        self.assertEqual(200, res.status_code)
        
        serializer_data = QuizRetrieveSerializer(instance=self.quiz).data
        res_data = json.loads(res.content)
        self.assertEqual(serializer_data, res_data)

    def test_answer_create_view(self):
        res = self.client.post(
            path="/quiz/answers/",
            data={"quiz":f"{self.quiz.id}", "content":"테스트답변"})
        self.assertEqual(201, res.status_code)
        
    def test_answer_list_view(self):
        self.test_answer_create_view()
        self.test_answer_create_view()
        res = self.client.get(path=f"/quiz/{self.quiz.id}/answers/")
        self.assertEqual(200, res.status_code)
        
        answer_arr = Answer.objects.filter(quiz=self.quiz.id)
        test_data = {'quiz': answer_arr[0].quiz.content}
        res_data = json.loads(res.content)
        self.assertEqual(test_data['quiz'], res_data['quiz'])
        self.assertEqual(2, res_data['count'])