from django.urls import path
from . import views

urlpatterns = [
    path('pt_sessions/', views.pt_sessions, name='pt_sessions'),
    path('pt_sessions/create', views.create_appointment, name='create_appointment'),
]