from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.title
