from django.db import models

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    scheldule = models.CharField(max_length=100, null=True)
    time = models.TimeField(auto_now_add=True, null=True)
    message = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.name