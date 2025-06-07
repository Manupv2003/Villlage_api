from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Job, Worker
from .serializers import JobSerializer, WorkerSerializer

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class WorkerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
