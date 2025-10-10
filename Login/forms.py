# transactions/forms.py

# home/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'Username'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border rounded',
            'placeholder': 'Password'
        })
    )

class RegisterForm(UserCreationForm):
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border rounded',
        'placeholder': 'Email'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-full p-2 border rounded',
        'placeholder': 'Username'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border rounded',
        'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'w-full p-2 border rounded',
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user






# from django import forms
# from Persistence.models import IncomeTransaction, OutgoingTransaction, Category

# FREQUENCY_CHOICES = [
#     ('Diário', ' Diário'),
#     ('Semanal', ' Semanal'),
#     ('Mensal', ' Mensal'),
#     ('Anual', ' Anual'),
# ]

# class IncomeTransactionForm(forms.ModelForm):
#     description = forms.CharField(
#         label="Descrição",
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
#             'placeholder': 'Ex: Salário, Freelance, etc.'
#         })
#     )

#     value = forms.DecimalField(
#         label="Valor (R$)",
#         widget=forms.NumberInput(attrs={
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
#             'placeholder': 'Ex: 2500.00'
#         })
#     )

#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         label="Categoria",
#         widget=forms.Select(attrs={
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white'
#         })
#     )

#     frequency = forms.ChoiceField(
#         label="Frequência",
#         choices=FREQUENCY_CHOICES,
#         widget=forms.Select(attrs={
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white'
#         })
#     )

#     class Meta:
#         model = IncomeTransaction
#         fields = ['description', 'value', 'category', 'frequency']


# # === FORMULÁRIO DE GASTOS ===
# class OutgoingTransactionForm(forms.ModelForm):
#     description = forms.CharField(
#         label="Descrição",
#         max_length=100,
#         widget=forms.TextInput(attrs={
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
#             'placeholder': 'Ex: Conta de luz, Restaurante, etc.'
#         })
#     )

#     value = forms.DecimalField(
#         label="Valor (R$)",
#         widget=forms.NumberInput(attrs={
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent',
#             'placeholder': 'Ex: 150.75'
#         })
#     )

#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         label="Categoria",
#         widget=forms.Select(attrs={
#             'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent bg-white'
#         })
#     )

#     class Meta:
#         model = OutgoingTransaction
#         fields = ['description', 'value', 'category']
