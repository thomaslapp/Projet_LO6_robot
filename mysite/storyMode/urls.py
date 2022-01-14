from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.mode_histoire, name='mode_histoire'),
    path('storyOne/', include('storyOne.urls')),
]