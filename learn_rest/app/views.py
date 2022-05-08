from django.shortcuts import redirect, render

# Create your views here.


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task
from app import serializers

@api_view(['GET'])
def index(req):
    some_dic = {
        'List': '/list/',
        'Detail View': '/<str:pk>',
        'create': '/task-create/',
        'update': '/task-update/<str:pk>',
        'delete': '/task-delete/<str: pk>',
    }
    return Response(some_dic)

@api_view(['GET'])
def taskList(req):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(req, pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(req):
    serializer = TaskSerializer(data = req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(req, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance =task, data = req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(req, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("/task-list")
    