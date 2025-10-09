from django.db import models
from django.db import transaction
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    current_balance = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client.username
    
    class Meta:
        db_table = 'clients'
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        db_table = 'categories'
        ordering = ['name']
    
class IncomeTransaction(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BigIntegerField()
    carried_out_at = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client.username} - {self.value}"

    class Meta:
        db_table = 'income_transactions'
        ordering = ['-carried_out_at']

class OutgoingTransaction(models.Model):

    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.BigIntegerField()
    carried_out_at = models.DateTimeField(auto_now_add=True)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.client.username} - {self.value}"

    class Meta:
        db_table = 'outcome_transactions'
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
