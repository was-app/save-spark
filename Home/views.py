from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home/dashboard.html')

def index(request):
    return redirect('home:dashboard') 
