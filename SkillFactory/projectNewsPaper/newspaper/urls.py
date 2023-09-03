from django.urls import path
from .views import PostsList, PostDetail, Posts, PostDetailView, PostCreateView, PostUpdateView, \
    PostDeleteView, CategoryListView

app_name = 'newspaper'
urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('news/', Posts.as_view()),
    path('category/<int:pk>/', CategoryListView.as_view()),


]