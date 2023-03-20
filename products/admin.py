from django.contrib import admin
from .models import Products, Categories, Appointments


# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

    ordering = ('name',)


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
    )

    ordering = ('category',)


class AppointmentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_time',)

    ordering = ('user',)


admin.site.register(Categories, CategoriesAdmin)

admin.site.register(Products, ProductsAdmin)

admin.site.register(Appointments, AppointmentsAdmin)
