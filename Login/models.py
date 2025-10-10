from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_client')
    current_balance = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.description} ({self.get_frequency_display()}) - R$ {self.amount}"