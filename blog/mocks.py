
from django.http import Http404

class Post():

    POSTS = [
        {'id':1,'title':'first article', 'body':'my first article'},
        {'id':2,'title':'second article', 'body':'my second article'},
        {'id':3,'title':'third article', 'body':'my third article'},
    ]

    @classmethod
    def all(cls):
        return cls.POSTS

    @classmethod
    def find(cls, id):
        try:
            return cls.POSTS[int(id) - 1]
        except:
            #if we put return instead, we'll not raise and exception but a ''(empty space..)
            raise Http404('Sorry, post {} not found.'.format(id))
