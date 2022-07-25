from django.contrib import admin
from .models import Post, Reply
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ["title", "category", 'date']
    search_fields = ('title', )
    list_filter = ["date", "category", ]


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ["get_title", "get_author", "status", 'date']
    search_fields = ('post__title', )
    list_filter = ["date", 'status', "post__author", ]

    def get_author(self, obj):
        return obj.post.author
    get_author.short_description = 'Post Author'

    def get_title(self, obj):
        return obj.post.title
    get_title.short_description = 'Post Title'
