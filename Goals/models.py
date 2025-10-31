from django.db import models
from django.conf import settings

class Goal(models.Model):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='goals')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    target_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
