
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetail, PostCreateView, PostUpdateView, \
    PostDeleteView, ReplayCreateView, ReplyListView, ReplyDeleteView, AcceptReply


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('post/<int:pk>', PostDetail.as_view(), name='post'),
    path('add_post/', PostCreateView.as_view(),
         name='post_create'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:pk>/reply', ReplayCreateView.as_view(), name='reply_create'),
    path('replies', ReplyListView.as_view(), name='replies'),
    path('reply/<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply_delete'),
    path('reply/<int:pk>/accept/', AcceptReply, name='reply_accept'),

]
