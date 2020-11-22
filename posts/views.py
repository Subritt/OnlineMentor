from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Query

class PostListView(ListView):
    model = Query
    template_name = 'posts/home.html'
    context_object_name = 'queries'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Query