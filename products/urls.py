from django.urls import path
from . import views

urlpatterns = [
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('pt_sessions/', views.pt_sessions, name='pt_sessions'),
]