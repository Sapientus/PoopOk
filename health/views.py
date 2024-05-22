# health/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import HealthSurvey
from .forms import HealthSurveyForm

@login_required
def health_survey(request):
    if request.method == 'POST':
        form = HealthSurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
            return redirect('health_survey_results')
    else:
        form = HealthSurveyForm()
    return render(request, 'health/health_survey.html', {'form': form})

@login_required
def health_survey_results(request):
    surveys = HealthSurvey.objects.filter(user=request.user)
    return render(request, 'health/health_survey_results.html', {'surveys': surveys})

@login_required
def medical_services(request):
    return render(request, 'health/medical_services.html')