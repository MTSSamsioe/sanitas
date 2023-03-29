from django.urls import path
from . import views

urlpatterns = [
    path('pt_sessions/', views.pt_sessions, name='pt_sessions'),
    path('pt_sessions/edit/<appointment_id>',
         views.edit_appointment, name='edit_appointment'),
    path('pt_sessions/delete/<appointment_id>',
         views.delete_appointment, name='delete_appointment'),
]
