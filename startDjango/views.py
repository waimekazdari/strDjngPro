from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse('hello world')
    return render(request, 'home.html')