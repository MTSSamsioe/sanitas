''' All of url names are taken from
Code institute project
Boutique ado
https://github.com/Code-Institute-Solutions/boutique_ado_v1/
blob/250e2c2b8e43cccb56b4721cd8a8bd4de6686546/bag/urls.py'''

from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_bag_item, name='add_bag_item'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]
