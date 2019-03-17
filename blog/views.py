from django.shortcuts import render

def index(request):

    posts =['post1', 'post2', 'post3']
    return render(request, 'blog/index.html',{'posts':posts})
