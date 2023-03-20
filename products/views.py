from django.shortcuts import render, get_object_or_404, redirect
from .models import Products , Categories
from checkout.models import Order_item, Order
from .models import Appointments
from django.contrib import messages
from .forms import AppointmentsForm

#Validation 
from django.core.exceptions import ValidationError

# Time packages
from datetime import datetime, timedelta
from django.utils import timezone

# Create your views here.



def pt_sessions(request):
    """ A view to show all personal trainer sessions and appointments"""
    form = AppointmentsForm()
    scheduled_sessions = len(Appointments.objects.filter(user=request.user).values_list())
    quantity = sum(i[0] for i in Order_item.objects.filter(user=request.user).values_list('quantity'))
    pt_sessions = Products.objects.filter(category=2)
    # Appointment
    appointments = Appointments.objects.filter(user=request.user)
    available_appointments = quantity - scheduled_sessions
    # Time variables 
    change_time = timezone.now() + timedelta(minutes=60)
    # Appoint ment form
    context = {
        'pt_sessions': pt_sessions,
        # 'quantity': quantity,
        'form': form,
        'appointments': appointments,
        'scheduled_sessions': scheduled_sessions,
        # 'appointments_time': appointments_time,
        'change_time': change_time,
        'available_appointments': available_appointments,
    }

    return render(request, 'products/pt_sessions.html', context)
    

def create_appointment(request):
    ''' A view to Make an appoitment for personal trainer'''
    form = AppointmentsForm(request.POST, user=request.user)
    scheduled_sessions = len(Appointments.objects.filter(user=request.user).values_list())
    quantity = sum(i[0] for i in Order_item.objects.filter(user=request.user).values_list('quantity'))
    pt_sessions = Products.objects.filter(category=2)
    # Appointment
    appointments = Appointments.objects.filter(user=request.user)
    available_appointments = quantity - scheduled_sessions
    # Time variable
    change_time = timezone.now() + timedelta(minutes=60)
    if request.method == 'POST':
        if form.is_valid():

            form_save = form.save()
            form_save.user = request.user
            form_save.save()
            messages.success(request,
                                '''Your
                                appointment with one of our personal
                                trainers has been saved''')
            
        else:

            messages.error(request, '''Something went wrong
                            please press "Create button" again''')
            

        context = {
            'pt_sessions': pt_sessions,
            'form': form,
            'appointments': appointments,
            'scheduled_sessions': scheduled_sessions,
            'change_time': change_time,
            'available_appointments': available_appointments,
        }

    return render(request, 'products/pt_sessions.html', context)


def edit_appointment(request, appointment_id):
    ''' View to change date and time on appointments with personal trainer '''

    appointment = get_object_or_404(Appointments, id=appointment_id)
    form = AppointmentsForm(instance=appointment)

    if request.method == 'POST':
        form = AppointmentsForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment was successfully changed')
            return redirect('/products/pt_sessions/')
        else:
            messages.error(request, 'Something went wrong')
           
    
    context = {
        'form': form,
        'appointment': appointment,
    }
    return render(request, 'products/edit_session.html', context)


def delete_appointment(request, appointment_id):

    appointment = get_object_or_404(Appointments, id=appointment_id)
    appointment.delete()
    messages.success(request, 'Your appointment has been canceled')
    return redirect('/products/pt_sessions/')