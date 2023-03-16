from django.shortcuts import render, get_object_or_404, redirect
from .models import Products , Categories
from checkout.models import Order_item, Order
from django.contrib import messages
from .forms import AppointmentsForm

# Create your views here.

def pt_sessions(request):
    """ A view to show all personal trainer sessions and appointments"""

    quantity = Order_item.objects.filter(user=request.user).values_list('quantity')
    
    pt_sessions = Products.objects.filter(category=2)

    # Appoint ment form
    form = AppointmentsForm()
    context = {
        'pt_sessions': pt_sessions,
        'quantity': quantity,
        'form': form,
    }

    return render(request, 'products/pt_sessions.html', context)
    

def create_appointment(request):
    form = AppointmentsForm(request.POST)
    if form.is_valid():

        form_save = form.save()
        form_save.user = request.user
        form_save.save()
        messages.success(request,
                             '''Your
                             appointment with one of our personal
                             trainers has been saved''')
        return redirect('/products/pt_sessions.html/')
    else:

        messages.error(request, '''Something went wrong
                           please press "Create button" again''')
    
    context = {
        'form': form
    }

    return render(request, 'products/pt_sessions.html', context)

