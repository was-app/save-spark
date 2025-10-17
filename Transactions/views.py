# transactions/views.py

from .forms import IncomeTransactionForm, OutgoingTransactionForm
from .models import FinancialTransactionProcessor
from Persistence.services.transaction_service import TransactionService
from Persistence.models import Category
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
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    service = TransactionService()

    if request.method == 'POST':
        transaction_type = request.POST.get('transaction_type')
        transaction_id = request.POST.get('transaction_id')
        new_category_name = request.POST.get('category')

        if transaction_type == 'income':
            transaction = service.get_income_by_id(transaction_id)
        else:
            transaction = service.get_outgoing_by_id(transaction_id)

        if transaction and new_category_name:
            transaction.category = new_category_name
            if transaction_type == 'income':
                service.update_income(transaction=transaction)
            else:
                service.update_outgoing(transaction=transaction)

        return redirect('view_all')

    income_transactions = service.get_incomes_from_user(user)
    outgoing_transactions = service.get_outgoings_from_user(user)
    

    grouped = {}
    for t in income_transactions:
        cat_name = t.category if t.category else "Sem Categoria"
        t.type = "income"
        grouped.setdefault(cat_name, []).append(t)

    for t in outgoing_transactions:
        cat_name = t.category if t.category else "Sem Categoria"
        t.type = "outgoing"
        grouped.setdefault(cat_name, []).append(t)

    categories = [cat.name for cat in Category.objects.all()]

    context = {
        'grouped_transactions': grouped,
        'categories': categories,
    }

    return render(request, 'transactions/view_all.html', context)