from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView


app_name = BlogConfig.name
urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create_post'),
    path('', PostListView.as_view(), name='list'),
    path('view/<int:pk>/', PostDetailView.as_view(), name='view_post'),
    path('edit/<int:pk>/', PostUpdateView.as_view(), name='edit_post')
]
