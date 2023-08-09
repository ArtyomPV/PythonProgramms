from django.contrib import admin
from .models import Order, Product, ProductOrder, Staff

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(ProductOrder)
admin.site.register(Staff)
