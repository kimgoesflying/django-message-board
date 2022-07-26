
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetail, PostCreateView, PostUpdateView, PostDeleteView, ReplayCreateView, ReplyListView


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('add_post/', PostCreateView.as_view(),
         name='post_create'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),

    path('<int:pk>/reply', ReplayCreateView.as_view(), name='reply_create'),
    path('replies', ReplyListView.as_view(), name='replies'),
]
