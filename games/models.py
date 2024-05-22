# games/models.py
from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class GameSession(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player1 = models.ForeignKey(User, related_name='player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(User, related_name='player2', on_delete=models.CASCADE)
    winner = models.ForeignKey(User, related_name='winner', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.player1.username} vs {self.player2.username} - {self.game.name}'
