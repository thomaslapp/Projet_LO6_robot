from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render 
import sys
from subprocess import run, PIPE

def get_formRobot(request):
    return render(request, 'template_formRobot.html')

def execScript(request):
    out = run([sys.executable,'C:\\Users\\thoma\\Desktop\\Cours\\LP\\LO6 robot\\GitHub\\Projet_LO6_robot\\mysite\\formRobot\\MYSCRIPT.py'], shell=True,stdout=PIPE)
    return HttpResponse(out)