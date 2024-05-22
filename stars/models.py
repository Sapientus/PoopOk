# stars/models.py
from django.db import models
from django.contrib.auth.models import User

class Star(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.stars} stars'

class Action(models.Model):
    ACTION_TYPES = [
        ('THROW', 'Кинуть какаху'),
        ('FLUSH', 'Смыть оппонента'),
        ('BOTH', 'Высрать и смыть'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(User, related_name='target', on_delete=models.CASCADE)
    action_type = models.CharField(max_length=5, choices=ACTION_TYPES)
    stars_used = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.action_type} - {self.target.username}'
