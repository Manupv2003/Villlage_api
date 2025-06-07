from rest_framework import serializers
from .models import Job, Worker

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ['id', 'name', 'contact_number']

class JobSerializer(serializers.ModelSerializer):
    workers = WorkerSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'workers']
