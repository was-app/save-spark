from django import forms
from Persistence.models import IncomeTransaction, OutgoingTransaction, Category

FREQUENCY_CHOICES = [
    ('Diário', ' Diário'),
    ('Semanal', ' Semanal'),
    ('Mensal', ' Mensal'),
    ('Anual', ' Anual'),
    ('Único', ' Único')
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

    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(type='income').order_by('name'),
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Populate choices dynamically at runtime
        self.fields['category'].choices = [
            (str(category.id), category.name)
            for category in Category.objects.filter(type='income').order_by('name')
        ]


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
        queryset=Category.objects.filter(type='outgoing').order_by('name'),
        label="Categoria",
        widget=forms.Select(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white'
        })
    )

    class Meta:
        model = OutgoingTransaction
        fields = ['description', 'value', 'category']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Populate choices dynamically at runtime
    #     self.fields['category'].choices = [
    #         (str(category.id), category.name)
    #         for category in Category.objects.filter(type='Gasto').order_by('name')
    #     ]