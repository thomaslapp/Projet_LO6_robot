from django.urls import include, path
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.mode_histoire, name='mode_histoire'),
    path('storyOne/', include('storyOne.urls')),
]