from django.db import models
from django.contrib.auth.models import User

class LocalNews(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    token = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.token
