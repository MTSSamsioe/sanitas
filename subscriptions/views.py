from django.shortcuts import render, redirect
import stripe
import json
from django.http import JsonResponse
from djstripe.models import Product, Plan
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request):
  return render(request, "test.html")


def stripe_subscriptions(request):
    """ A view to show all stripe gym subscriptions"""
    plans = Plan.objects.all()
    subscriptions = Product.objects.all()
    context = {
        'plans': plans,
        'subscriptions': subscriptions,
        
    }

    return render(request, 'subscriptions/stripe_subscriptions.html', context)