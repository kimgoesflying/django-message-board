from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ['-date']
    list_display = ["title", "category", 'date']
    search_fields = ('title', )
    list_filter = ["date", "category", ]
