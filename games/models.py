# games/models.py
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GameSession(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return self.name

