# games/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_game_session, name='create_game_session'),
    path('sessions/', views.game_session_list, name='game_session_list'),
]
