from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from .filters import PostFilter
# Create your views here.


class PostListView(ListView):
    model = Post
    ordering = '-date'
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(
            self.request.GET, queryset=self.get_queryset())
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return PostFilter(self.request.GET, queryset=queryset).qs


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'
