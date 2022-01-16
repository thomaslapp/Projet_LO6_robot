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
    filePath = './gamesPage/jeux/' + request.POST.get('nomExo') + '.py'
    print(filePath)
    saveout = sys.stdout
    fsock = open('out.log', 'w')
    sys.stdout = fsock
    try:
        exec(open(filePath).read())
    except Exception as error:
        print(error)
    
    sys.stdout = saveout
    fsock.close()
    fsockR = open('out.log', 'r')
    text = fsockR.read()
    fsockR.close()
    return render(request, 'gamesPage.html', {'logs':text})
    ##out = run([sys.executable,filePath], shell=True,stdout=PIPE)
    ##return HttpResponse(out)