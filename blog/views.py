from django.shortcuts import render

posts =[
    {'id':1,'title':'first article', 'body':'my first article'},
    {'id':2,'title':'second article', 'body':'my second article'},
    {'id':3,'title':'third article', 'body':'my third article'},
]
def index(request):

    #posts= []
    return render(request, 'blog/index.html',{'posts':posts})


def details(request,id):
    return render(request, 'blog/details.html', {'post': posts[int(id) - 1]})
