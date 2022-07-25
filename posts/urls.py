
from django.contrib import admin
from django.urls import path
from .views import PostListView, PostDetail, PostCreateView


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('add_post/', PostCreateView.as_view(),
         name='post_create'),
]
