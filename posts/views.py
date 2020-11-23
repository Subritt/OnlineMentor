from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from .models import Query

class PostListView(ListView):
    model = Query
    template_name = 'posts/home.html'
    context_object_name = 'queries'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Query

class PostCreateView(CreateView):
    model = Query
    fields = ['title', 'content']