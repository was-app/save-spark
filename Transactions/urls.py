from django.urls import path
from . import views

urlpatterns = [
    path('recurrent/', views.register_recurrent_transaction, name='recurrent_transaction'),
    path('extra/', views.register_extra_transaction, name='extra_transaction'),
]