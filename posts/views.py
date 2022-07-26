from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Reply
from .filters import PostFilter
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
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


class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('posts')
    permission_required = ('posts.add_post')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        response = super().form_valid(form)
        return response


class PostUpdateView(UpdateView):
    template_name = 'posts/post_update.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'posts/post_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('posts')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class ReplyListView(ListView):
    model = Reply
    ordering = '-date'
    template_name = 'posts/reply_list.html'
    context_object_name = 'replies'
    paginate_by = 2


class ReplayCreateView(CreateView):
    template_name = 'posts/reply_create.html'
    form_class = ReplyForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.post.id})
