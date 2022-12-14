from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializers
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def CreateTask(request: Request):
    data = request.data
    serializers = TaskSerializers(data=data)

    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    else:
        return Response(serializers.errors)


@api_view(['GET'])
def Get_Task(request: Request, id):
    try:
        tasks = Task.objects.get(id=id)
        serializers = TaskSerializers(tasks)
        return Response(serializers.data)
    except Task.DoesNotExist:
        return Response({'result':'Task not found'})


@api_view(['GET'])
def Get_All_Task(request: Request):
    tasks = Task.objects.all()
    serializers = TaskSerializers(tasks, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def Remove_Task(request: Request, id):
    tasks = Task.objects.get(id=id)
    tasks.delete()
    return Response({'result':'The task has been deleted'})

@api_view(['POST'])
def Update_Task(request: Request, id):
    try:
        data = request.data
        task = Task.objects.get(id=id)
        serializer = TaskSerializers(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    except Task.DoesNotExist:
        return Response({'result':'Task not found'})