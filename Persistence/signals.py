# Persistence/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.label == "Persistence":
        categories = [
            {'name': 'Salário', 'type': 'income'},
            {'name': 'Investimentos', 'type': 'income'},
            {'name': 'Freelance', 'type': 'income'},
            {'name': 'Outros', 'type': 'income'},
            {'name': 'Alimentação', 'type': 'outgoing'},
            {'name': 'Moradia', 'type': 'outgoing'},
            {'name': 'Transporte', 'type': 'outgoing'},
            {'name': 'Lazer', 'type': 'outgoing'},
            {'name': 'Saúde', 'type': 'outgoing'},
            {'name': 'Vaidade', 'type': 'outgoing'},
            {'name': 'Outros', 'type': 'outgoing'},
        ]
        for cat in categories:
            Category.objects.get_or_create(name=cat['name'], type=cat['type'])
