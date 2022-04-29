from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView


urlpatterns = [

    path("home/", PostListView.as_view(), name="blog_home"),
    path('post/<str:slug>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_create")
]