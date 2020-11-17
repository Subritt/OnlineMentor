from django.shortcuts import render
from .models import Query

def home(request):
    context = {
        'queries': Query.objects.all()
    }
    return render(request, 'posts/home.html', context)