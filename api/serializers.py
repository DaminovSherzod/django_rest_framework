from rest_framework import serializers
from .models import Task

class TaskSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    task = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    status = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id',instance.id)
        instance.task = validated_data.get('task', instance.task)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance