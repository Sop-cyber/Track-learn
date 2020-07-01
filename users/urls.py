"""Defin URL patterns for users"""
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # Registration page.
    path('register/', views.register, name='register'),
    # Include default auth urls.
    # path('', include('django.contrib.auth.urls')),
]