# transactions/views.py

from .forms import IncomeTransactionForm, OutgoingTransactionForm
from django.shortcuts import render, redirect


def add_income(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    
    if request.method == 'POST':
        form = IncomeTransactionForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.client = request.user
            income.save()
            return redirect('Home:dashboard') 
    else:
        form = IncomeTransactionForm()
        
    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'Renda'})

def add_outgoing(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = OutgoingTransactionForm(request.POST)
        if form.is_valid():
            outgoing = form.save(commit=False)
            outgoing.client = request.user
            outgoing.save()
            return redirect('Home:dashboard')
    else:
        form = OutgoingTransactionForm()

    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'Gasto'})