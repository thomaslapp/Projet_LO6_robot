from django.http import HttpResponseRedirect
from django.shortcuts import render

def menu_principal(request):
    return render(request, 'mainMenu.html')