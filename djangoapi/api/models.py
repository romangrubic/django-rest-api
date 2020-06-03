from django.db import models
from datetime import datetime

# Create your models here.
class Python(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link = models.URLField(max_length = 200)
    question_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question


class JavaScript(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link = models.URLField(max_length = 200)
    question_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question


class HTML(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link = models.URLField(max_length = 200)
    question_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question


class GIT(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    link = models.URLField(max_length = 200)
    question_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.question