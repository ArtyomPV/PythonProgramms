from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.urls import reverse_lazy, resolve
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import EmailMultiAlternatives


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
class PostCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'newspaper/post_create.html'
    permission_required = 'newspaper.add_post'
    form_class = PostForm


class PostUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'newspaper/post_create.html'
    permission_required = 'newspaper.change_post'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте который мы
    # собираемся редактировать
    def get_object(self, **rwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'newspaper/post_delete.html'
    permission_required = 'newspaper.delete_post'
    queryset = Post.objects.all()
    success_url = reverse_lazy('newspaper:posts')


class CategoryListView(ListView):
    model = Post
    template_name = 'newspaper/category.html'
    context_object_name = 'posts'
    ordering = ['-data_post_creation']
    paginate_by = 3

    def get_queryset(self):
        self.id = resolve(self.request.path_info).kwargs['pk']
        # print(resolve(self.request.path_info))
        c = Category.objects.get(id=self.id)
        queryset = Post.objects.filter(category=c)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # print(user.email)
        category = Category.objects.get(id=self.id)
        subscribed = category.subscribers.filter(email=user.email)
        if not subscribed:
            context['category'] = category
        return context


def subscribe_to_category(request, pk):
    user = request.user
    print('======user=========')
    print(user)
    category = Category.objects.get(id=pk)
    if not category.subscribers.filter(id=user.id).exists():
        category.subscribers.add(user)
        email = user.email
        html_content = render_to_string(
            'newspaper/subscribed.html',
            {
                'category': category,
                'user': user
            }
        )
        msg = EmailMultiAlternatives(
            subject=f'{category} subscription',
            body='',
            from_email='artyom.pv@yandex.ru',
            to=[email, ],
        )
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        return redirect('newspaper:posts')
    return redirect('newspaper:posts')


@login_required
def unsubscribe_from_category(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    if category.subscribers.filter(id=user.id).exists():
        category.subscribers.remove(user)
    return redirect('newspaper:posts')
