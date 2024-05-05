from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

#creating logic to handle the routes 

def home(request):
    return HttpResponse('<h1> Blog Home </h1>')
