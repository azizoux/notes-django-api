from rest_framework import serializers
from .models import Task, Note


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('id', 'title', 'description', 'is_completed')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Note
        fields=('id', 'title', 'subtitle', 'body')
