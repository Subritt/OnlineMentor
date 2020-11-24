from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Query

class PostListView(ListView):
    model = Query
    template_name = 'posts/home.html'
    context_object_name = 'queries'
    ordering = ['-date_posted']
    paginate_by = 9

class PostDetailView(DetailView):
    model = Query

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Query
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Query
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Query
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
