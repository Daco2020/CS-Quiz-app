from django.db   import models
from cs_quiz.apps.util.time_stamp import TimeStampModel


class Category(models.Model):
    content = models.CharField(max_length=100)
    depth = models.IntegerField(default=0)

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
    level = models.IntegerField(default=0)
    tag = models.ManyToManyField('Tag', through=QuizTag, related_name="quizzes")

    class Meta:
        db_table = 'quizzes'


class Answer(TimeStampModel):
    quiz = models.ForeignKey('Quiz', on_delete=models.CASCADE)
    reference_url = models.URLField(null=True)
    content = models.CharField(max_length=500)
    correct_point = models.IntegerField(default=0)
    
    class Meta: 
        db_table = 'answers'