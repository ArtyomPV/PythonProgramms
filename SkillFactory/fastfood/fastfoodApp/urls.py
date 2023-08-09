from django.urls import path
from .views import ProductsList, ProductDetail

urlpatterns = [
    path('', ProductsList.as_view()), # класс ProductsList надо предоставить класс в
    # виде view, для этого вызываем метод as_view
    path('<int:pk>', ProductDetail.as_view()),  # pk -- это первичный ключ товара,
    # который будет выводиться у нас в шаблон
]
