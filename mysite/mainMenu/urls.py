from django.urls import path

from . import views

urlpatterns = [
    path('', views.menu_principal, name='menu_principal'),
]