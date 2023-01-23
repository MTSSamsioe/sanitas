from django.shortcuts import render
from .models import Subscriptions, Pt_sessions

# Create your views here.

def subscriptions(request):
    """ A view to show all gym subscriptions"""

    subscriptions = Subscriptions.objects.all()

    context = {
        'subscriptions': subscriptions,
    }

    return render(request, 'products/subscriptions.html', context)