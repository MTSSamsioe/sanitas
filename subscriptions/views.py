from django.conf import settings
from django.shortcuts import render, redirect
import stripe
import json
from django.http import JsonResponse
from .models import StripeCustomer
from djstripe.models import Product, Plan
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@login_required
def stripe_subscriptions(request):
    """ A view to show all stripe gym subscriptions"""
    plans = Plan.objects.all()
    subscriptions = Product.objects.all()
    context = {
        'plans': plans,
        'subscriptions': subscriptions,
        
    }

    return render(request, 'subscriptions/stripe_subscriptions.html', context)

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        print(JsonResponse(stripe_config, safe=False))
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        print(stripe.api_key)
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancel/',
                payment_method_types=['card'],
                mode='subscription',
                line_items=[
                    {
                        'price': settings.STRIPE_PRICE_ID,
                        'quantity': 1,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})