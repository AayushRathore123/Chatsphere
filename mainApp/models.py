from tkinter import CASCADE
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
    name = models.CharField(max_length=200, null = True)
    email = models.EmailField(unique = True, null = True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null = True, default = "avatar1.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    

class Room(models.Model):
    host = models.ForeignKey(User, on_delete = models.SET_NULL, null = True)
    topic = models.ForeignKey('Topic', on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length=200)
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, related_name="participants", blank = True)
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated','-created']
    def __str__(self):
        return self.body[0:50]
    
class EVENT(models.Model):
    E_id = models.IntegerField()
    name = models.CharField(max_length=64,default="None")
    purpose = models.CharField(max_length=1000)
    date = models.DateField(("Date"), default=datetime.date.today)
    time = models.TimeField(("time"), default=datetime.datetime.now())
    place = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"Event {self.E_id} is scheduled on {self.date} at {self.time} \n on the topic {self.purpose} at {self.place}"
