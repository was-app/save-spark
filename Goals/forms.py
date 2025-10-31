from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    name = forms.CharField(
        label="Nome da Meta",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ex: Viagem para a praia'
        })
    )

    target_amount = forms.DecimalField(
        label="Valor Alvo (R$)",
        widget=forms.NumberInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
            'placeholder': 'Ex: 5000.00'
        })
    )

    target_date = forms.DateField(
        label="Data Alvo",
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white',
            'type': 'date'
        })
    )

    class Meta:
        model = Goal
        fields = ['name', 'target_amount', 'target_date', 'description']
