from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import LatinScript, HebWord
import string

def latinEntry(request):
    text = LatinScript.objects.all()
    context = {
        'text': text
    }
    return render(request, 'base.html', context)
   
def hebWord(request):
    long_url = request.POST['long_url']
    short_url = ''
    HebWord.objects.create()
    return HttpResponseRedirect(reverse(':base'))