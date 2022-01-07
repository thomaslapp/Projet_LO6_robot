from django.urls import path

from . import views

urlpatterns = [
    path('', views.page_jeux, name='page_jeux'),
]