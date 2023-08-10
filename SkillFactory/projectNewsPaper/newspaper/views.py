from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'newspaper/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-data_post_creation')


class PostDetail(DetailView):
    model = Post
    template_name = 'newspaper/post.html'
    context_object_name = 'post'
