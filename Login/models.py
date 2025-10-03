from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    current_balance = models.BigIntegerField(default=0)