import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from blog.models import Post
from config.settings import MEDIA_ROOT, MEDIA_URL


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blog:list')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blog:list')
