# health/models.py
from django.db import models
from django.contrib.auth.models import User

class HealthSurvey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    bowel_movements_per_day = models.PositiveIntegerField()
    stool_consistency = models.CharField(max_length=50)
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} - {self.date}'
