# stars/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('balance/', views.star_balance, name='star_balance'),
    path('action/', views.perform_action, name='perform_action'),
]

