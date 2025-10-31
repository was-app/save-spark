from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('add-goals/', views.add_goals, name='add_goals'),
    path('view-goals/', views.view_goals, name='view_goals'),
]