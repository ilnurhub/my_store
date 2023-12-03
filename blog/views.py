from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blog:list')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
