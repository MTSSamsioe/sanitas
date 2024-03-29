''' Class names and structure is taken from
Code institute project lessons Boutique ado
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/admin.py
'''


from django.contrib import admin
from .models import Order, Order_item


class OrderItemAdminInline(admin.TabularInline):
    model = Order_item
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)
    readonly_fields = (
        'order_number',
        'date',
        'total',

        )

    fields = ('full_name', 'user_profile',
              'email', 'adress',
              'post_code', 'city',
              'order_number', 'date', 'total',
              )

    list_display = ('order_number',
                    'full_name', 'date', 'total')

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
