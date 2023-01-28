from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_bag_item, name='add_bag_item'),
    path('update/<item_id>/', views.update_bag, name='update_bag'),
]
