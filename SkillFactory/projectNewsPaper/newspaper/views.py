from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'newspaper/posts.html'
    context_object_name = 'posts'
    ordering = ['-data_post_creation']
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'newspaper/post.html'
    context_object_name = 'post'


class PostsView(View):
    def get(self, request):
        posts = Post.models.order_by('-data_post_creation')
        p = Paginator(posts, 2)
        posts = p.get_page(request.GET.get('page', 1))
        data = {
            'posts': posts,
        }
        return render(request, 'newspaper/posts.html', data)
