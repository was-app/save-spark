# Transactions/forms.py

from django import forms
from Persistence.models import IncomeTransaction, OutgoingTransaction, Category

class IncomeTransactionForm(forms.ModelForm):
    # Puxa as categorias do banco de dados para o usuário poder escolher
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categoria",
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'})
    )

    class Meta:
        model = IncomeTransaction
        fields = ['value', 'category']
        widgets = {
            'value': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded', 
                                              'placeholder': 'Valor da Renda',
            }),
        }
        labels = {
            'value': 'Valor',
        }


class OutgoingTransactionForm(forms.ModelForm):
    # Puxa as categorias do banco de dados para o usuário poder escolher
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categoria",
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'})
    )

    class Meta:
        model = OutgoingTransaction
        fields = ['value', 'category']
        widgets = {
            'value': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded',
                                              'placeholder': 'Valor do Gasto',
            }),
        }
        labels = {
            'value': 'Valor',
        }