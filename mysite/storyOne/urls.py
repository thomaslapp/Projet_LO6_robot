from django.urls import path

from . import views

urlpatterns = [
    path('', views.histoire_un, name='histoire_un'),
]