from django.urls import path
from .views import RegisterView, LoginView, LogoutView

app_name = 'sign'

urlpatterns = [
   path('login/', LoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('register/', RegisterView.as_view(), name='register')
]
