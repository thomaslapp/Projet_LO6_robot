from django.urls import path

from . import views

urlpatterns = [
    path('', views.mode_histoire, name='mode_histoire'),
]