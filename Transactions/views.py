# transactions/views.py
from .forms import IncomeTransactionForm, OutgoingTransactionForm
from .models import FinancialTransactionProcessor
from Persistence.services.transaction_service import TransactionService
from Persistence.models import Category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Persistence.services.category_service import CategoryService
import logging
from django.contrib import messages


def add_income(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = IncomeTransactionForm(request.POST)
        if form.is_valid():
            # income = form.save(commit=False)
            income = form.cleaned_data
            tmp = FinancialTransactionProcessor()
            tmp.register_income(user=request.user, value=income['value'], category=income['category'], description=income['description'], frequency=income['frequency'])
            return redirect('home:dashboard')
        else:
            return HttpResponse(form.errors)
    else:
        form = IncomeTransactionForm()
        
    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'income', 'type_name': 'Renda'})

def add_outgoing(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = OutgoingTransactionForm(request.POST)
        if form.is_valid():
            # outgoing = form.save(commit=False)
            outgoing = form.cleaned_data
            tmp = FinancialTransactionProcessor()
            tmp.register_outgoing(user=request.user, value=outgoing['value'], category=outgoing['category'], description=outgoing['description'])
            return redirect('home:dashboard')
        else:
            return HttpResponse(form.errors)
    else:
        form = OutgoingTransactionForm()

    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'outgoing', 'type_name': 'Gasto'})

def view_all(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    service = FinancialTransactionProcessor()

    if request.method == 'POST':
        action = request.POST.get('action')
        category_service = FinancialTransactionProcessor()
        transaction_type = request.POST.get('transaction_type')
        transaction_id = request.POST.get('transaction_id')

        if action == 'delete':
            service.delete_transaction(request.user, transaction_type, transaction_id)
            messages.success(request, f'Transação deletada com sucesso!')
            

        elif action == 'update':
            new_category_id = request.POST.get('category')
            category = category_service.get_categories_by_id(new_category_id)
            if category:
                try:
                    service.update_transaction_category(transaction_type, transaction_id, category)
                    messages.success(request, f'Transação atualizada com sucesso!')
                except category.DoesNotExist:
                    messages.error(request, "Não foi possível atualizar a Transação")

        return redirect('view_all')

    income_transactions, outgoing_transactions = service.get_transactions(user)
    

    grouped = {}
    for t in income_transactions:
        cat_name = t.category.name if t.category else "Sem Categoria"
        t.type = "income"
        grouped.setdefault(cat_name, {'transactions': [], 'total': 0})
        grouped[cat_name]['transactions'].append(t)
        grouped[cat_name]['total'] += t.value

    for t in outgoing_transactions:
        cat_name = t.category.name if t.category else "Sem Categoria"
        t.type = "outgoing"
        grouped.setdefault(cat_name, {'transactions': [], 'total': 0})
        grouped[cat_name]['transactions'].append(t)
        grouped[cat_name]['total'] += t.value

    context = {
        'grouped_transactions': grouped,
        'income_categories': Category.objects.filter(type='income'),
        'outgoing_categories': Category.objects.filter(type='outgoing'),
    }

    return render(request, 'transactions/view_all.html', context)