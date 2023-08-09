from django.utils import timezone
from django.views.generic import ListView, DetailView
from .models import Product


class ProductsList(ListView):
    model = Product
    template_name = 'fastfoodApp/products.html'  # имя шаблона, в котором будет
    # лежать HTML, в нем будут инструкции, о том как будут выводиться наши объекты
    context_object_name = 'products'  # имя списка в котором лежат все объекты,
    # его нужно указать, чтобы обратиться к самому списку объктов через HTML шаблон
    queryset = Product.objects.order_by('-price')

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(
            timezone.now())  # добавим переменную текущей даты time_now
        context[
            'value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context


# создаём представление, в котором будут детали конкретного отдельного товара
class ProductDetail(DetailView):
    model = Product  # модель всё та же, но мы хотим получать детали конкретно
    # отдельного товара
    template_name = 'fastfoodApp/product.html'  # название шаблона будет product.html
    context_object_name = 'product'  # название объекта
