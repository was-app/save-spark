from django import forms
from Persistence.models import IncomeTransaction, OutgoingTransaction, Category

FREQUENCY_CHOICES = [
    ('Diário', ' Diário'),
    ('Semanal', ' Semanal'),
    ('Mensal', ' Mensal'),
    ('Anual', ' Anual'),
]

class IncomeTransactionForm(forms.ModelForm):
    description = forms.CharField(
        label="Descrição",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ex: Salário, Freelance, etc.'
        })
    )

    value = forms.DecimalField(
        label="Valor (R$)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ex: 2500.00'
        })
    )

    category = forms.CharField(
        label="Categoria",
        widget=forms.Select(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white'
        })
    )

    frequency = forms.ChoiceField(
        label="Frequência",
        choices=FREQUENCY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white'
        })
    )

    class Meta:
        model = IncomeTransaction
        fields = ['description', 'value', 'category', 'frequency']


#   === FORMULÁRIO DE GASTOS ===
class OutgoingTransactionForm(forms.ModelForm):
    description = forms.CharField(
        label="Descrição",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ex: Conta de luz, Restaurante, etc.'
        })
    )

    value = forms.DecimalField(
        label="Valor (R$)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ex: 150.75'
        })
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Categoria",
        widget=forms.Select(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white'
        })
    )

    class Meta:
        model = OutgoingTransaction
        fields = ['description', 'value', 'category']