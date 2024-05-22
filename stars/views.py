# stars/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Star, Action
from .forms import ActionForm

@login_required
def star_balance(request):
    star = Star.objects.get(user=request.user)
    return render(request, 'stars/star_balance.html', {'star': star})

@login_required
def perform_action(request):
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if form.is_valid():
            action = form.save(commit=False)
            action.user = request.user
            action.save()
            star = Star.objects.get(user=request.user)
            star.stars -= action.stars_used
            star.save()
            return redirect('star_balance')
    else:
        form = ActionForm()
    return render(request, 'stars/perform_action.html', {'form': form})
