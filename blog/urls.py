from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostCommentView


urlpatterns = [

    path("home/", PostListView.as_view(), name="blog_home"),
    path('post/<str:slug>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_create"),
    path('post/<str:slug>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<str:slug>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('post/<str:slug>/comment/', PostCommentView.as_view(), name="post_comments"),
]