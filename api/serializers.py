from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.Serializer):
    task = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    status = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)