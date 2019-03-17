from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('hello world')
    return render(request, 'home.html')

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contact.html')
