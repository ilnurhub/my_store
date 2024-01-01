from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'first_name', 'last_name', 'phone')
    list_filter = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
