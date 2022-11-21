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
