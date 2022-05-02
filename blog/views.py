import imp
from pyexpat import model
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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



# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = "post"

def PostDetailView(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image', 'slug', 'category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image', 'slug', 'category']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Post
    # fields = ['title', 'content', 'image', 'slug', 'category']
    success_url = "/"


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    # success_url = "/"
    template_name = "blog/post_comment_form.html"

    def form_valid(self, form):
        form.instance.name = self.request.user
        form.instance.post_slug = self.kwargs['slug']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'slug': self.kwargs['slug']})

# YOU ADDED THIS FROM THE WEB
def post_detail(request, slug):
    template_name = 'blog/web_post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})







