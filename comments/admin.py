from django.contrib import admin

from comments.models import Comments, Users


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'parent', 'text', 'created_at']

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'home_page']
