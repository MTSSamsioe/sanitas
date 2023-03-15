from django.shortcuts import render, get_object_or_404
from .models import Products , Categories
from checkout.models import Order_item, Order

# Create your views here.

def pt_sessions(request):
    """ A view to show all personal trainer sessions and appointments"""

    quantity = Order_item.objects.filter(user=request.user).values_list('quantity')

    pt_sessions = Products.objects.filter(category=2)
    context = {
        'pt_sessions': pt_sessions,
        'quantity': quantity,
    }

    return render(request, 'products/pt_sessions.html', context)
    

