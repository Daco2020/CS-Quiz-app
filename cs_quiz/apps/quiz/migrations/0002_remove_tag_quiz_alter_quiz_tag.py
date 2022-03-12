# Generated by Django 4.0.1 on 2022-03-12 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='quiz',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='quizzes', through='quiz.QuizTag', to='quiz.Tag'),
        ),
    ]
