from django.db import models

class LocalNews(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
