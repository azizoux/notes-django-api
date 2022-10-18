from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import Task, Note
from api.serializers import TaskSerializer, NoteSerializer


@csrf_exempt
def tasks_api(request, id=0):

    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)

    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to Add departement", safe=False)

    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task = Task.objects.get(id=task_data['id'])
        task_serializer = TaskSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def notes_api(request, id=0):

    if request.method == 'GET':
        notes = Note.objects.all()
        notes_serializer = NoteSerializer(notes, many=True)
        return JsonResponse(notes_serializer.data, safe=False)

    elif request.method == 'POST':
        note_data = JSONParser().parse(request)
        note_serializer = NoteSerializer(data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Added note successfully", safe=False)
        return JsonResponse("Failed to Add Note", safe=False)

    elif request.method == 'PUT':
        note_data = JSONParser().parse(request)
        note = Note.objects.get(id=note_data['id'])
        note_serializer = NoteSerializer(note, data=note_data)
        if note_serializer.is_valid():
            note_serializer.save()
            return JsonResponse("Updated note Successfully", safe=False)
        return JsonResponse("Failed to Update Note", safe=False)

    elif request.method == 'DELETE':
        note = Note.objects.get(id=id)
        note.delete()
        return JsonResponse("Deleted Note Successfully", safe=False)
