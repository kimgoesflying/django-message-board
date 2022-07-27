from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Reply
from .filters import PostFilter, ReplyFilter
from .forms import PostForm, ReplyForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.http import HttpResponseRedirect
# Create your views here.

from .tasks import send_mail_post_reply_task


class PostListView(FilterView):
    model = Post
    ordering = '-date'
    template_name = 'posts/posts_list.html'
    context_object_name = 'posts'
    filterset_class = PostFilter
    paginate_by = 5


class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/post_create.html'
    form_class = PostForm
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        response = super().form_valid(form)
        return response


class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'posts/post_update.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'posts/post_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('posts')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class ReplyListView(LoginRequiredMixin, FilterView):
    context_object_name = 'replies'
    template_name = 'posts/reply_list.html'
    filterset_class = ReplyFilter
    paginate_by = 10

    def get_queryset(self):
        return Reply.objects.filter(post__author_id=self.request.user).order_by("-date")


class ReplayCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/reply_create.html'
    form_class = ReplyForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author_id = self.request.user.id
        response = super().form_valid(form)
        send_mail_post_reply_task.delay(self.object.pk)
        return response

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.object.post.id})


class ReplyDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'posts/reply_delete.html'
    queryset = Reply.objects.all()
    success_url = reverse_lazy('replies')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Reply.objects.get(pk=id)


@login_required
def AcceptReply(request, *args, **kwargs):
    pk = kwargs.get('pk')
    reply = Reply.objects.get(pk=pk)
    reply.accept_reply()
    return redirect('/replies')

    # if reply.is_accepted:
    #     send_mail_status.delay(reply.pk)
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
