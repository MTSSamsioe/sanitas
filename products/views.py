from django.shortcuts import render, get_object_or_404
from .models import Products , Categories

# Create your views here.

def subscriptions(request):
    """ A view to show all gym subscriptions"""

    subscriptions = Products.objects.filter(category=1)
    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'products/subscriptions.html', context)


def pt_sessions(request):
    """ A view to show all personal trainer sessions"""

    pt_sessions = Products.objects.filter(category=2)
    context = {
        'pt_sessions': pt_sessions,
    }

    return render(request, 'products/pt_sessions.html', context)
    