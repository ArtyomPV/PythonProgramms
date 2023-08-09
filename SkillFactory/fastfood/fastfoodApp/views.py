from django.views.generic import ListView, DetailView
from .models import Product


class ProductsList(ListView):
    model = Product
    template_name = 'fastfoodApp/products.html'  # имя шаблона, в котором будет
    # лежать HTML, в нем будут инструкции, о том как будут выводиться наши объекты
    context_object_name = 'products'  # имя списка в котором лежат все объекты,
    # его нужно указать, чтобы обратиться к самому списку объктов через HTML шаблон


# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно
    # отдельного товара
    template_name = 'fastfoodApp/product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта
