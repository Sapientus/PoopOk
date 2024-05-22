# health/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('survey/', views.health_survey, name='health_survey'),
    path('results/', views.health_survey_results, name='health_survey_results'),
    path('services/', views.medical_services, name='medical_services'),
]
