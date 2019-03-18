from django.shortcuts import render

#from mocks import la class Post
from .mocks import Post
def index(request):

    posts= Post.all()
    return render(request, 'blog/index.html',{'posts':posts})


def details(request,id):
    post =  Post.find(id)
    return render(request, 'blog/details.html', {'post': post})
