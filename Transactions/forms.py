from django import forms

TRANSACTION_TYPE = [
    ('expense', 'Gasto'),
    ('income', 'Renda')
]

CATEGORY_CHOICES = [
    ('business', 'Business'),
    ('vanity', 'Vanity'),
    ('extra', 'Extra'),
    ('luxury', 'Luxury'),
    ('job', 'Job'),
    ('food', 'Food'),
]

class TransactionForm(forms.Form):
    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPE, label="Tipo", required=True)
    name = forms.CharField(max_length=100, label="Nome", required=True)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, label="Valor", required=True)
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Categoria", required=True)