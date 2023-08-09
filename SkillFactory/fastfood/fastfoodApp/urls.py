from  django.urls import  path
from .views import ProductsList

urlpatterns = [
    path('', ProductsList.as_view()) # класс ProductsList надо предоставить класс в
    # виде view, для этого вызываем метод as_view
]
