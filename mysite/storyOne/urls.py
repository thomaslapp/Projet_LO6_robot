from django.urls import path

from . import views

urlpatterns = [
    path('', views.histoire_un, name='histoire_un'),
    path('storyOne/execScript/', views.execScript),
]