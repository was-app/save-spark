from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from . import views
# Create your views here.

urlpatterns = [
    path('', views.redirect_login),
    path('login/', views.user_login, name='Login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout')
]