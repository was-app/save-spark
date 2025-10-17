from django.urls import path
from . import views

urlpatterns = [
    path('add-income/', views.add_income, name='add_income'),
    path('add-outgoing/', views.add_outgoing, name='add_outgoing'),
    path('view-all/', views.view_all, name='view_all'),
]