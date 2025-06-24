from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LocalNews, Device
from .serializers import LocalNewsSerializer
from .utils import send_fcm_v1_notification
from firebase_admin import messaging

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
        # Get all device tokens from your database
        device_tokens = [d.token for d in Device.objects.all()]  # Example model
        send_fcm_v1_notification(
            token=device_tokens,  # or loop through tokens if sending one by one
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

def send_fcm_v1_notification(token, title, body):
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body,
            ),
            token=token,
        )
        response = messaging.send(message)
        return response
    except messaging.UnregisteredError:
        # Remove the token from your Device model
        from .models import Device
        Device.objects.filter(token=token).delete()
        print(f"Removed invalid FCM token: {token}")
    except Exception as e:
        print(f"FCM send error: {e}")

# Create your views here.
