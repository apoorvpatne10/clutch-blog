from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Apoorv',
        'title': 'Blog Post 1',
        'content': 'The first post content',
        'date_posted': 'September 1, 2018'
    },
    {
        'author': 'William',
        'title': 'Blog Post 2',
        'content': 'The second hokage',
        'date_posted': 'September 3, 2018'
    }
]

def home(request):
    context = {
        'post1': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
