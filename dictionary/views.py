from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Phonemes, HebWord

def home(request):
    return render(request, 'home.html')
   