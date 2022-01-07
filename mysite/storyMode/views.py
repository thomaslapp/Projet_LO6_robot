from django.http import HttpResponseRedirect
from django.shortcuts import render

def mode_histoire(request):
    return render(request, 'storyMode.html')