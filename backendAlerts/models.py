from django.db import models

# Create your models here.

class Alert(models.Model):
    name = models.CharField(max_length=40)
    date = models.DateTimeField()
    hasNotified = models.BooleanField()