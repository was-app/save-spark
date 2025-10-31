from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('connect-belvo/', views.connect_belvo, name='connect_belvo'),
    path('', views.index, name='index'),
]