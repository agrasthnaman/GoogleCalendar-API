from django.db import models

class User(models.Model):
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
