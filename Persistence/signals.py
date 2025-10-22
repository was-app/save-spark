# Persistence/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.label == "Persistence":
        categories = [
            {'name': 'Salário', 'type': 'Renda'},
            {'name': 'Investimentos', 'type': 'Renda'},
            {'name': 'Freelance', 'type': 'Renda'},
            {'name': 'Outros', 'type': 'Renda'},
            {'name': 'Alimentação', 'type': 'Gasto'},
            {'name': 'Moradia', 'type': 'Gasto'},
            {'name': 'Transporte', 'type': 'Gasto'},
            {'name': 'Lazer', 'type': 'Gasto'},
            {'name': 'Saúde', 'type': 'Gasto'},
            {'name': 'Vaidade', 'type': 'Gasto'},
            {'name': 'Outros', 'type': 'Gasto'},
        ]
        for cat in categories:
            Category.objects.get_or_create(name=cat['name'], type=cat['type'])
