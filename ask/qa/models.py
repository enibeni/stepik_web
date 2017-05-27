# -- coding: utf-8 --

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        new = Question.objects.order_by('added_at')
        return new

    def popular(self):
        popular = Question.objects.order_by('-rating')
        return popular


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(
            default=timezone.now)
    rating = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=255)
    likes = models.ForeignKey(User, blank=True, null=True, related_name='question_like')
    objects = QuestionManager()

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(
            default=timezone.now)
    question = models.ForeignKey(Question)
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.question.__str__()

    def publish(self):
        self.published_date = timezone.now()
        self.save()
