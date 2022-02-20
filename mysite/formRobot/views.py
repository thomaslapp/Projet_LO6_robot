from django.http import HttpResponseRedirect
from django.http.response import HttpResponse
from django.shortcuts import render 
import sys
from subprocess import run, PIPE

def get_formRobot(request):
    return render(request, 'template_formRobot.html')


def execScript(request):

    #print (request.POST.get('code'))
    filePath = '.\\MYSCRIPT.py';
    open(filePath, 'w').close()

    file_object = open(filePath, 'a')
    file_object.write(request.POST.get('code'));
    file_object.close();

    saveout = sys.stdout
    fsock = open('out.log', 'w')
    sys.stdout = fsock
    erreur = ""
    """
    with open("interface/scriptRobots/BaseQuestion.py") as programToExecute:
        try:
            exec(programToExecute.read())
        except Exception as error:
            erreur = error
    """
    try:    
        exec(open(filePath).read())
    except Exception as error:
        erreur = "Sortie erreur : " + str(error)
    
    
    sys.stdout = saveout
    fsock.close()
    fsockR = open('out.log', 'r')
    text = "Sortie standard : " + fsockR.read()

    fsockR.close()
    return render(request, 'template_formRobot.html', {'logs':text, 'error':erreur})

    ##out = run([sys.executable,filePath], shell=True,stdout=PIPE)
    ##return HttpResponse("")