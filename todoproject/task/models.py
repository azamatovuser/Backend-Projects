from django.db import models
from .constans import TASK


class Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=221)
    status = models.IntegerField(choices=TASK.STATUS.STATUS, default=TASK.STATUS.DEFAULT)
    priority = models.IntegerField(choices=TASK.PRIORITY.PRIORITY, default=TASK.PRIORITY.DEFAULT)
    deadline = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title