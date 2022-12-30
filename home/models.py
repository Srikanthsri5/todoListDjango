from django.db import models
# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDesc = models.CharField(max_length=2000)
    time = models.DateTimeField(auto_created = True)

    def __str__(self):
        return self.taskTitle