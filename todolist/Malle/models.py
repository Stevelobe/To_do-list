from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
    
class MalleTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MalleTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(MalleTag, blank=True)

    def __str__(self):
        return self.title
