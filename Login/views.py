from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Client

# Create your views here.
from .forms import *

def redirect_login(request):
    return redirect('Login')

def user_logout(request):
    logout(request)
    return redirect('Login')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                
                 # VAMOS ADICIONAR ESTA LINHA PARA TESTE:
                print("--- TENTANDO REDIRECIONAR AGORA ---")
                
                return redirect('home:dashboard')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            client = Client(client=user)
            return redirect('Login')
        else:
            messages.error(request, form.errors)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})