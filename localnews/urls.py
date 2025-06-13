from django.urls import path
from .views import LocalNewsListView, LocalNewsDetailView

urlpatterns = [
    path('news/', LocalNewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', LocalNewsDetailView.as_view(), name='news-detail'),
]