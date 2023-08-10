from django.urls import path
from  .views import PostsList, PostDetail

urlpatterns = [
    path('', PostsList.as_view()),
    path('post/<int:pk>', PostDetail.as_view())
]