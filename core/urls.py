from django.contrib import admin
from django.urls import path
from .views import dashboard, atualizar_status  

urlpatterns = [
    path('', view=dashboard, name='dashboard'),
]
