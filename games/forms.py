# F:\Нова папка (3)\PoopOk\games\forms.py
from django import forms
from .models import GameSession

class GameSessionForm(forms.ModelForm):
    class Meta:
        model = GameSession
        fields = ['name', 'score']
