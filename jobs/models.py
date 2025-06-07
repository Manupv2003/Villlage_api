from django.db import models

from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Worker(models.Model):
    job = models.ForeignKey(Job, related_name='workers', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.job.title})"

