from django.shortcuts import render
from rest_framework import generics
from .models import LocalNews
from .serializers import LocalNewsSerializer

class LocalNewsListView(generics.ListAPIView):
    queryset = LocalNews.objects.all().order_by('-date_posted')
    serializer_class = LocalNewsSerializer

class LocalNewsDetailView(generics.RetrieveAPIView):
    queryset = LocalNews.objects.all()
    serializer_class = LocalNewsSerializer

# Create your views here.
