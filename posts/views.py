from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django.views.generic.edit import FormMixin
from django import forms
from .models import Query, Reply
from ckeditor.widgets import CKEditorWidget
from .forms import CommentForm

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

class PostDetailView(FormMixin, DetailView):
    model = Query
    form_class = CommentForm
    slug_field = 'header'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        context['replies'] = Reply.objects.filter(post=self.object.id).order_by('-id')
        return context
    
    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect(settings.LOGIN_URL)

        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save(self.object, self.request.user)
        return super(PostDetailView, self).form_valid(form)

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
