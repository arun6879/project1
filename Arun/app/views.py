from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ak(request):
    return HttpResponse('<h1><marquee>Hi bro I am Banda</marquee></h1>')