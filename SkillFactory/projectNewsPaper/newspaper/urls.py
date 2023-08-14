from django.urls import path
from  .views import PostsList, PostDetail, Posts

app_name = 'newspaper'
urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('news/', Posts.as_view()),

]