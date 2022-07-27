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
    list_display = ["get_reply_author", "get_title",
                    "get_post_author", "is_accepted", 'date']
    search_fields = ('post__title', )
    list_filter = ["date", 'is_accepted', ]

    def get_reply_author(self, obj):
        return obj.author
    get_reply_author.short_description = 'Авток отклика'

    def get_post_author(self, obj):
        return obj.post.author
    get_post_author.short_description = 'Автор объявления'

    def get_title(self, obj):
        return obj.post.title
    get_title.short_description = 'заголовок объяыления'
