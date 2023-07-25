from django.db import models
from django.db.models import BooleanField


# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_add = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task
