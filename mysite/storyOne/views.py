from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse
import sys
from subprocess import run, PIPE
from .forms import NameForm

def histoire_un(request):
    return render(request, 'storyOne.html')

def execScript(request):
    print (request.POST.get('code'))
    filePath = '.\\MYSCRIPT.py'
    open(filePath, 'w').close()

    file_object = open(filePath, 'a')
    file_object.write(request.POST.get('code'));
    file_object.close();
    saveout = sys.stdout
    fsock = open('out.log', 'w')
    sys.stdout = fsock
    exec(open(filePath).read())
    sys.stdout = saveout
    fsock.close()
    fsockR = open('out.log', 'r')
    text = fsockR.read()
    fsockR.close()
    return render(request, 'storyOne.html', {'logs':text})