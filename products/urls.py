from django.urls import path
from . import views

urlpatterns = [
    path('pt_sessions/', views.pt_sessions, name='pt_sessions'),
]