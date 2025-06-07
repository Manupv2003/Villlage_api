from django.urls import path
from .views import JobListCreateAPIView, WorkerListCreateAPIView

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='jobs-list-create'),
    path('workers/', WorkerListCreateAPIView.as_view(), name='workers-list-create'),
]
