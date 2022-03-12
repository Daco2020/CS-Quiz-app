# Generated by Django 4.0.1 on 2022-03-12 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_remove_tag_quiz_alter_quiz_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='tag',
            field=models.ManyToManyField(related_name='quizzes', through='quiz.QuizTag', to='quiz.Tag'),
        ),
    ]