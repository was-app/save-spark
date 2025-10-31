from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Q
from Persistence.models import Category, IncomeTransaction, OutgoingTransaction

# Create your views here.
def category_list(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        action = request.POST.get('action')
        category_id = request.POST.get('category_id')
        name = request.POST.get('name')
        type_ = request.POST.get('type')

        if action == 'create' and name and type_:
            Category.objects.create(name=name, type=type_)
            messages.success(request, f'Categoria "{name}" criada com sucesso.')

        elif action == 'update' and category_id and name and type_:
            try:
                category = Category.objects.get(id=category_id)
                category.name = name
                category.type = type_
                category.save()
                messages.success(request, f'Categoria "{name}" atualizada com sucesso.')
            except Category.DoesNotExist:
                messages.error(request, "Categoria não encontrada.")

        elif action == 'delete' and category_id:
            try:
                category = Category.objects.get(id=category_id)
                has_transactions = IncomeTransaction.objects.filter(category=category).exists() \
                                   or OutgoingTransaction.objects.filter(category=category).exists()
                if has_transactions:
                    messages.error(request, "Não é possível deletar uma categoria com transações associadas.")
                else:
                    category.delete()
                    messages.success(request, f'Categoria "{category.name}" excluída com sucesso.')
            except Category.DoesNotExist:
                messages.error(request, "Categoria não encontrada.")

        return redirect('category_list')

    # GET request: show all categories
    categories = Category.objects.all().order_by('name')
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)