# games/forms.py
from django import forms
from .models import GameSession

class GameSessionForm(forms.ModelForm):
    class Meta:
        model = GameSession
        fields = ['game', 'player2']
