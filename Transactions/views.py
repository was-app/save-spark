from django.shortcuts import render, redirect
from .forms import TransactionForm

def register_recurrent_transaction(request):
    if not request.user.is_authenticated:
        return redirect('Login')

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = TransactionForm()

    return render(request, 'Transactions/transaction_form.html', {'form': form, 'title': 'Recurrent Transaction'})


def register_extra_transaction(request):
    if not request.user.is_authenticated:
        return redirect('Login')

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect('home')
    else:
        form = TransactionForm()

    return render(request, 'Transactions/transaction_form.html', {'form': form, 'title': 'Extra Transaction'})
