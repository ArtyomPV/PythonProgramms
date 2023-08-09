from django.views.generic import ListView
from .models import Post
# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'newspaper/posts.html'
    context_object_name = 'posts'
