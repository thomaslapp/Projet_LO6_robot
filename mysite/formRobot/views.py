from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render 
import sys
from subprocess import run, PIPE


from .forms import NameForm
def get_formRobot(request):
    
    form = NameForm()

    return render(request, 'name.html', {'form': form})


def execScript(request):
    print (request.POST.get('code'))
    filePath = '.\\MYSCRIPT.py'
    open(filePath, 'w').close()

    file_object = open(filePath, 'a')
    file_object.write(request.POST.get('code'));
    file_object.close();
    out = run([sys.executable,filePath], shell=True,stdout=PIPE)
    return HttpResponse(out)