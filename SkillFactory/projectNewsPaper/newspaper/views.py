from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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


# дженерик для получения деталей о товаре
class PostDetailView(DetailView):
    template_name = 'newspaper/post_detail.html'
    queryset = Post.objects.all()


# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в
# прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'newspaper/post_create.html'
    form_class = PostForm


class PostUpdateView(UpdateView):
    template_name = 'newspaper/post_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы
    # собираемся редактировать
    def get_object(self, **rwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'newspaper/post_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('newspaper:posts')
