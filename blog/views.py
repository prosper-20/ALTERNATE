from pyexpat import model
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "blog/index.html", context)


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "blog/index.html"



class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'slug', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


