from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Post


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blog:list')


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body', 'photo')
    success_url = reverse_lazy('blog:list')


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:list')
