from django.urls import path
from  .views import PostsList, PostDetail, PostsView

app_name = 'newspaper'
urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('news/', PostsView.as_view()),
]