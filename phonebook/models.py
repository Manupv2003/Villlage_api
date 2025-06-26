from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    house_name = models.CharField(max_length=100)  # Changed from 'address'
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.mobile}"


