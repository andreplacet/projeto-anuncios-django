from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(response):
    response = 'Ola Mundo!!'
    return HttpResponse(response)
