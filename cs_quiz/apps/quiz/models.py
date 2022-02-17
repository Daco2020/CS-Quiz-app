from django.db   import models
from django.forms import IntegerField
from cs_quiz.apps.util.time_stamp import TimeStampModel


class Category(models.Model):
    content = models.CharField(max_length=100)
    depth = models.IntegerField()

    class Meta:
        db_table = 'categories'


class QuizTag(models.Model):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'quiz_tags'


class Tag(models.Model):
    content = models.CharField(max_length=50)
    quiz = models.ManyToManyField('Quiz', through=QuizTag, related_name="tags")
    
    class Meta:
        db_table = 'tags'

        
class Quiz(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    level = models.IntegerField()
    tag = models.ManyToManyField('Tag', through=QuizTag, related_name="quizzes")

    class Meta:
        db_table = 'quizzes'


class Answer(TimeStampModel):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    reference_url = models.URLField()
    content = models.CharField(max_length=500)
    correct_point = IntegerField()
    
    class Meta: 
        db_table = 'answers'