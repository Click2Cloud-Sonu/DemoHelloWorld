from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def msg(request):

    return HttpResponse("Hellow World .!")
