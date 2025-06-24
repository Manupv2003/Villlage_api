from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LocalNews, Device
from .serializers import LocalNewsSerializer
from .utils import send_fcm_v1_notification

class LocalNewsListView(generics.ListAPIView):
    queryset = LocalNews.objects.all().order_by('-date_posted')
    serializer_class = LocalNewsSerializer

class LocalNewsDetailView(generics.RetrieveAPIView):
    queryset = LocalNews.objects.all()
    serializer_class = LocalNewsSerializer

class LocalNewsCreateView(generics.CreateAPIView):
    queryset = LocalNews.objects.all()
    serializer_class = LocalNewsSerializer

    def perform_create(self, serializer):
        news = serializer.save()
        device_tokens = [d.token for d in Device.objects.all()]
        send_fcm_v1_notification(
            tokens=device_tokens,
            title=news.title,
            body=news.short_description
        )

class RegisterDeviceView(APIView):
    def post(self, request):
        token = request.data.get('token')
        user = request.user if request.user.is_authenticated else None
        if token:
            Device.objects.update_or_create(token=token, defaults={'user': user})
            return Response({'status': 'registered'})
        return Response({'error': 'No token provided'}, status=400)
