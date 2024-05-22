# health/forms.py
from django import forms
from .models import HealthSurvey

class HealthSurveyForm(forms.ModelForm):
    class Meta:
        model = HealthSurvey
        fields = ['bowel_movements_per_day', 'stool_consistency', 'additional_notes']
