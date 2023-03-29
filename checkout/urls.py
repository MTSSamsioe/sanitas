'''
All code below is takne from Boutique ado walkthrough project
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/urls.py
'''
from django.urls import path
from .import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>',
         views.checkout_success, name='checkout_success'),
    path('wh/', webhook, name='webhook'),
    path('cache_checkout_data/',
         views.cache_checkout_data, name='cache_checkout_data'),
]
