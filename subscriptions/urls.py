from django.urls import path
from . import views
from django.http import JsonResponse



urlpatterns = [
    path('', views.stripe_subscriptions, name='stripe_subscriptions'),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
    path("cancel-sub", views.cancel_sub, name="cancel_sub"),

]
