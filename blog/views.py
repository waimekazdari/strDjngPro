from django.shortcuts import render

def index(request):

    #posts= []
    posts =[
        {'id':1,'title':'first article', 'body':'my first article'},
        {'id':2,'title':'second article', 'body':'my second article'},
        {'id':3,'title':'third article', 'body':'my third article'},
    ]
    return render(request, 'blog/index.html',{'posts':posts})
