from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Client = apps.get_model('Login', 'Client')

    user, created = User.objects.get_or_create(
        username='test',
        defaults={
            'email': 'test@example.com',
            'password': make_password('test'),
            'is_superuser': True,
            'is_staff': True,
        }
    )

    Client.objects.get_or_create(client=user, defaults={'current_balance': 1000})

def delete_default_user(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Client = apps.get_model('Login', 'Client')
    user = User.objects.filter(username='admin').first()
    if user:
        Client.objects.filter(client=user).delete()
        user.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_user, delete_default_user),
    ]
