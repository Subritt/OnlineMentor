from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
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

class UserPostListView(ListView):
    model = Query
    template_name = 'posts/user_posts.html'
    context_object_name = 'queries'
    paginate_by = 9

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Query.objects.filter(author=user).order_by('-date_posted')

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
