from django.contrib import admin
from .models import *
from itertools import chain


class PostAdmin(admin.ModelAdmin):
    def category_names(self, obj):
        a = obj.category.values_list('name')
        return list(chain.from_iterable(a))

    list_display = ('author', 'post_type', 'title', 'text', 'rating_post', 'category_names')


admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
