from django.db import models
from django.db import transaction
from django.contrib.auth.models import User

FREQUENCY_CHOICES = [
    ('Diário', 'Diário'),
    ('Semanal', 'Semanal'),
    ('Mensal', 'Mensal'),
    ('Anual', 'Anual'),
    ('Único', 'Único'),
]

# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='persistence_client')
    current_balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.username
    
    class Meta:
        db_table = 'clients'
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=[('income', 'Income'), ('outgoing', 'Outgoing')], null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        ordering = ['name']
    
class IncomeTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField()
    carried_out_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.client.username} - {self.value}"

    class Meta:
        db_table = 'income_transactions'
        ordering = ['-carried_out_at']

class OutgoingTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.FloatField()
    carried_out_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.CharField(max_length=50, choices=FREQUENCY_CHOICES, blank=True, null=True)

    def __str__(self):
        return f"{self.client.username} - {self.value}"

    class Meta:
        db_table = 'outgoing_transactions'
        ordering = ['-carried_out_at']

class BaseRepository:
    def __init__(self, model: models.Model):
        self.model = model

    @transaction.atomic
    def create(self, **kwargs):
        return self.model.objects.create(**kwargs)

    def get(self, **filters):
        return self.model.objects.get(**filters)

    def filter(self, **filters):
        return self.model.objects.filter(**filters)

    @transaction.atomic
    def update(self, instance, **kwargs):
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @transaction.atomic
    def delete(self, instance):
        instance.delete()
