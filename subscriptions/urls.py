from django.urls import path
from . import views

urlpatterns = [
    path('stripe_subscriptions/', views.stripe_subscriptions, name='stripe_subscriptions'),
]
