from django.http import HttpResponseRedirect
from django.shortcuts import render

def page_jeux(request):
    return render(request, 'gamesPage.html')