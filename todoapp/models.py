from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoItem(models.Model):
    user = models.ForeignKey(
        User, null=True,  blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=156, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True)
    date_cancelled = models.DateTimeField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
