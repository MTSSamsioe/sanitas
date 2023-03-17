from django.shortcuts import render, get_object_or_404, redirect
from .models import Products , Categories
from checkout.models import Order_item, Order
from .models import Appointments
from django.contrib import messages
from .forms import AppointmentsForm

# Create your views here.

def pt_sessions(request):
    """ A view to show all personal trainer sessions and appointments"""
    appointments = len(Appointments.objects.filter(user=request.user).values_list())
    quantity = sum(i[0] for i in Order_item.objects.filter(user=request.user).values_list('quantity'))
    appointments_time = Appointments.objects.filter(user=request.user).values_list('date_time')
    pt_sessions = Products.objects.filter(category=2)

    # Appoint ment form
    form = AppointmentsForm()
    context = {
        'pt_sessions': pt_sessions,
        'quantity': quantity,
        'form': form,
        'appointments': appointments,
        'appointments_time': appointments_time,
    }

    return render(request, 'products/pt_sessions.html', context)
    

def create_appointment(request):
    ''' A view to create an appoitment for personal trainer'''
    form = AppointmentsForm(request.POST, user=request.user) # user=request.user
    if form.is_valid():

        form_save = form.save()
        form_save.user = request.user
        form_save.save()
        messages.success(request,
                             '''Your
                             appointment with one of our personal
                             trainers has been saved''')
        #return redirect('/products/pt_sessions.html/')
    else:

        messages.error(request, '''Something went wrong
                           please press "Create button" again''')
    
    context = {
        'form': form
    }

    return render(request, 'products/pt_sessions.html', context)

