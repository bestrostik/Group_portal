from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .models import CustomUser
from .forms import CustomUserCreationForm
import calendar
from datetime import datetime, timedelta

# Create your views here.
class RegisterView(CreateView): # - RegisterView for registering new users
    model = CustomUser
    template_name = 'auth_sys/register_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('main')

class CustomLoginView(LoginView):
    template_name = 'auth_sys/login.html'
    success_url = reverse_lazy('main')

def timeline_calendar(request):
    # Початкова дата - поточний місяць
    today = datetime.today()
    start_date = today - timedelta(days=30)  # Відобразити 30 днів до поточного
    end_date = today + timedelta(days=60)    # І 60 днів після

    timeline = []
    current_date = start_date
    while current_date <= end_date:
        timeline.append({
            "date": current_date,
            "day": current_date.day,
            "weekday": calendar.day_name[current_date.weekday()],
            "month": current_date.strftime('%B')
        })
        current_date += timedelta(days=1)

    return render(request, 'default_pages\main.html', {
        'timeline': timeline,
        'today': today,
    })