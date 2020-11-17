from django.shortcuts import render

posts = [
    {
        'author': 'Jane Doe',
        'title': 'Query 1',
        'content': 'FIrst query',
        'date_posted': 'November 17, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Query 2',
        'content': 'Second query',
        'date_posted': 'November 18, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'posts/home.html', context)