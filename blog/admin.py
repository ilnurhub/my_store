from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'views_count')
    list_filter = ('title',)
    search_fields = ('title', 'body')
