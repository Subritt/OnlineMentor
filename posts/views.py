from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Query

class PostListView(ListView):
    model = Query
    template_name = 'posts/home.html'
    context_object_name = 'queries'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Query

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Query
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Query
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)