from django.urls import path
from . import views

urlpatterns = [
    path('stripe_subscriptions/', views.stripe_subscriptions, name='stripe_subscriptions'),
    path("checkout_sub", views.checkout_sub, name="checkout_sub"),
    path("create-sub", views.create_sub, name="create sub"),
    path("complete", views.complete, name="complete"),
    
]
