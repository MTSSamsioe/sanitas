from django.shortcuts import render, get_object_or_404
from .models import Subscriptions, Pt_sessions

# Create your views here.

def subscriptions(request):
    """ A view to show all gym subscriptions"""

    subscriptions = Subscriptions.objects.all()
    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'products/subscriptions.html', context)


def pt_sessions(request):
    """ A view to show all personal trainer sessions"""

    pt_sessions = Pt_sessions.objects.all()
    context = {
        'pt_sessions': pt_sessions,
    }

    return render(request, 'products/pt_sessions.html', context)