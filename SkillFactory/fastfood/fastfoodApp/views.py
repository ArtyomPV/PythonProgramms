from django.shortcuts import render
from django.views.generic import ListView
from .models import Product

class ProductsList(ListView):
    model = Product
    template_name = 'fastfoodApp/products.html' #имя шаблона, в котором будет
    # лежать HTML, в нем будут инструкции, о том как будут выводиться наши объекты
    context_object_name = 'products' #имя списка в котором лежат все объекты,
    # его нужно указать, чтобы обратиться к самому списку объктов через HTML шаблон


