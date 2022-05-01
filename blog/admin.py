from django.contrib import admin
from .models import  Category, Post, Comment
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "date_posted"]

admin.site.register(Post, PostAdmin)
admin.site.register(Category)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'date_added', 'active')
    list_filter = ('active', 'date_added')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


