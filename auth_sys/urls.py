from django.urls import path
from auth_sys import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('calendar/', views.timeline_calendar, name='timeline_calendar'),
]
