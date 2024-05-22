# games/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, GameSession
from .forms import GameSessionForm

@login_required
def create_game_session(request):
    if request.method == 'POST':
        form = GameSessionForm(request.POST)
        if form.is_valid():
            game_session = form.save(commit=False)
            game_session.player1 = request.user
            game_session.save()
            return redirect('game_session_list')
    else:
        form = GameSessionForm()
    return render(request, 'games/create_game_session.html', {'form': form})

@login_required
def game_session_list(request):
    game_sessions = GameSession.objects.filter(player1=request.user) | GameSession.objects.filter(player2=request.user)
    return render(request, 'games/game_session_list.html', {'game_sessions': game_sessions})
