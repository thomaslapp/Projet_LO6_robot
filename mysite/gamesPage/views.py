from os import system
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.shortcuts import render 
import sys
from subprocess import run, PIPE

def page_jeux(request):
    return render(request, 'gamesPage.html')

def execScript(request):
    filePath = '.\\gamesPage\\jeux\\' + request.POST.get('nomExo') + ".py"
    print(filePath)
    out = run([sys.executable,filePath], shell=True,stdout=PIPE)
    return HttpResponse(out)