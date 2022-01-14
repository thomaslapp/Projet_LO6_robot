<<<<<<< HEAD
from django.urls import include, path
=======
from django.urls import path, include
>>>>>>> 02192d8d85f560a921519d70e0c2b4ed94ec2eb5

from . import views

urlpatterns = [
    path('', views.mode_histoire, name='mode_histoire'),
    path('storyOne/', include('storyOne.urls')),
]