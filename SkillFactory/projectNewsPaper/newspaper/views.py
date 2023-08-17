from django.views import View
from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post
from .filters import PostFilter
from .forms import PostForm

# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'newspaper/posts.html'
    context_object_name = 'posts'
    ordering = ['-data_post_creation']
    paginate_by = 3
    form_class = PostForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['post_types'] = Post.POSTS
        context['form'] = PostForm()
        return context

    def get_queryset(self):
        return PostFilter(self.request.GET, super().get_queryset()).qs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из
        # POST-запроса
        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не накосячил, то сохраняем
            # новый товар
            form.save()
        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'newspaper/post.html'
    context_object_name = 'post'


class Posts(View):
    def get(self, request):
        posts = Post.objects.order_by('-data_post_creation')
        p = Paginator(posts, 3)
        posts = p.get_page(request.GET.get('page', 1))
        data = {
            'posts': posts,
        }
        return render(request, 'newspaper/posts.html', data)
