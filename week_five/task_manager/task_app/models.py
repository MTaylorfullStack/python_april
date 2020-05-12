from django.db import models

# Create your models here.

class Task(models.Model):
    task = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
