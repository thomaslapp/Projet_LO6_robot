"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('formRobot/', include('formRobot.urls')),
    path('', include('mainMenu.urls')),
    path('gamesPage', include('gamesPage.urls')),
    path('storyMode/', include('storyMode.urls')),
    path('storyOne', include('storyOne.urls')),
<<<<<<< HEAD
    path('admin/', admin.site.urls),
=======
    path('admin', admin.site.urls),
>>>>>>> 02192d8d85f560a921519d70e0c2b4ed94ec2eb5
]
