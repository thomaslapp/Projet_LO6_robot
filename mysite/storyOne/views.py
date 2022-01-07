from django.http import HttpResponseRedirect
from django.shortcuts import render

def histoire_un(request):
    return render(request, 'storyOne.html')