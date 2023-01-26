from django.contrib import admin
from .models import Products, Categories


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
   list_display =(
        'name',
    )
ordering = ('name,')


class ProductsAdmin(admin.ModelAdmin):
   list_display =(
        'name',
        'category',
    )
ordering = ('category,')

admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Products, ProductsAdmin)
