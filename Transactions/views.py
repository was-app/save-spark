# transactions/views.py

from .forms import IncomeTransactionForm, OutgoingTransactionForm
from .models import FinancialTransactionProcessor
from Persistence.services.transaction_service import TransactionService
from django.shortcuts import render, redirect
from django.http import HttpResponse


def add_income(request):
    if not request.user.is_authenticated:
        return redirect('login') 
    
    print(request)
    if request.method == 'POST':
        form = IncomeTransactionForm(request.POST)
        if form.is_valid():
            # income = form.save(commit=False)
            income = form.cleaned_data
            tmp = TransactionService()
            tmp.register_income(client=request.user, value=income['value'], category=income['category'])
            return redirect('home:dashboard')
        else:
            return HttpResponse(form.errors)
    else:
        form = IncomeTransactionForm()
        
    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'Renda'})

def add_outgoing(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = OutgoingTransactionForm(request.POST)
        if form.is_valid():
            # outgoing = form.save(commit=False)
            outgoing = form.cleaned_data
            tmp = TransactionService()
            tmp.register_outgoing(client=request.user, value=outgoing['value'], category=outgoing['category'])
            return redirect('home:dashboard')
    else:
        form = OutgoingTransactionForm()

    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'Gasto'})

def view_all(request):
    pass