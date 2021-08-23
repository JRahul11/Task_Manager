from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class TaskModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    priority = models.IntegerField(default=-1)
    date = models.DateTimeField(default=now)
    iscompleted = models.BooleanField(default=False)

    def __str__(self):
        return self.title
