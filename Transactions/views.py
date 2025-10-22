# transactions/views.py
from .forms import IncomeTransactionForm, OutgoingTransactionForm
from .models import FinancialTransactionProcessor
from Persistence.services.transaction_service import TransactionService
from Persistence.models import Category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Persistence.services.category_service import CategoryService

def add_income(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = IncomeTransactionForm(request.POST)
        if form.is_valid():
            # income = form.save(commit=False)
            income = form.cleaned_data
            tmp = TransactionService()
            tmp.register_income(client=request.user, value=income['value'], category=income['category'], description=income['description'], frequency=income['frequency'])
            return redirect('home:dashboard')
        else:
            return HttpResponse(form.errors)
    else:
        form = IncomeTransactionForm()
        
    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'Renda'})

def add_outgoing(request):
    if not request.user.is_authenticated:
        return redirect('login')

    categories = TransactionService().get_category_by_type('Gasto')

    if request.method == 'POST':
        form = OutgoingTransactionForm(request.POST)
        if form.is_valid():
            # outgoing = form.save(commit=False)
            outgoing = form.cleaned_data
            tmp = TransactionService()
            tmp.register_outgoing(client=request.user, value=outgoing['value'], category=outgoing['category'], description=outgoing['description'])
            return redirect('home:dashboard')
    else:
        form = OutgoingTransactionForm()

    return render(request, 'transactions/add_transaction.html', {'form': form, 'type': 'Gasto', 'categories': categories})

def view_all(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    user = request.user
    service = TransactionService()

    if request.method == 'POST':

        category_service = CategoryService()
        transaction_type = request.POST.get('transaction_type')
        transaction_id = request.POST.get('transaction_id')
        new_category_name = request.POST.get('category')
        category = category_service.get_category_by_name(new_category_name)

        if transaction_type == 'income':
            transaction = service.get_income_by_id(transaction_id)
        else:
            transaction = service.get_outgoing_by_id(transaction_id)

        if transaction and category:
            transaction.category = category
            if transaction_type == 'income':
                service.update_income(transaction, **{'category': category})
            else:
                service.update_outgoing(transaction, **{'category': category})

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