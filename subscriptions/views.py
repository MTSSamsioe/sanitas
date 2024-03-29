from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
import stripe
import json
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .models import StripeCustomer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from subscriptions.models import StripeCustomer
from django.contrib import messages

import os
if os.path.exists("env.py"):
    import env
''' Some variable names and logic is taken
from https://testdriven.io/blog/django-stripe-subscriptions/
'''


def stripe_subscriptions(request):
    """ A view to show all stripe gym subscriptions"""
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_product_info = settings.STRIPE_PRODUCT_INFO
    products_stripe = stripe.Product.retrieve(stripe_product_info)
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        subscription = (stripe.Subscription
                        .retrieve(stripe_customer.stripeSubscriptionId))
        context = {
            'products_stripe': products_stripe,
            'subscription': subscription,
        }
        return render(request,
                      'subscriptions/stripe_subscriptions.html', context)
    except Exception:
        pass
        messages.error(request, 'Could not find an active\
 subscription, try logging in first or subscribe to one')
    context = {'products_stripe': products_stripe, }
    return render(request, 'subscriptions/stripe_subscriptions.html', context)


'''
Some variable names and logic is taken
from https://testdriven.io/blog/django-stripe-subscriptions/
'''


@csrf_exempt
def cancel_sub(request):
    if request.user.is_authenticated:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Cancel subscription on stripe
            subscription = (StripeCustomer
                            .objects.values_list('stripeSubscriptionId')[0][0])
            stripe.Subscription.delete(subscription,)
            messages.success(request, 'Your subscription is canceled')
        except Exception:
            messages.error(request, 'Unable to cancel \
                           subscription, Subscription id was not in database')
            return redirect('/subscriptions/')
        try:
            # Delete subscription info from databases
            user = request.user
            subscription_django = StripeCustomer.objects.filter(user=user)
            subscription_django.delete()
            messages.success(request, 'Your subscription \
                             is deleted from database')
        except Exception:
            messages.error(request, 'Unable to delete subscription \
                           from database, Could not find customer')
            return redirect('/')
        return redirect('/')
    else:
        return redirect('/accounts/login/')


'''
Function below is taken
from https://testdriven.io/blog/django-stripe-subscriptions/
'''


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        print(JsonResponse(stripe_config, safe=False))
        return JsonResponse(stripe_config, safe=False)


'''
Function below is taken
from https://testdriven.io/blog/django-stripe-subscriptions/
'''


@csrf_exempt
@login_required
def create_checkout_session(request):
    if not StripeCustomer.objects.filter(user=request.user).exists():
        if request.method == 'GET':
            if os.environ.get('DEVELOPMENT'):
                domain_url = 'https://8000-mtssamsioe-sanitas\
-4vmeom2cqnk.ws-eu93.gitpod.io/subscriptions/'
            else:
                domain_url = 'https://sanitas-gym.herokuapp.com/subscriptions/'
            stripe.api_key = settings.STRIPE_SECRET_KEY
            try:
                checkout_session = stripe.checkout.Session.create(
                    client_reference_id=(request.user.id if
                                         request.user.is_authenticated
                                         else None),
                    success_url=domain_url + 'success?session_id=\
{CHECKOUT_SESSION_ID}',
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
    else:
        messages.error(request, 'Your already have an active subscription')
        return redirect('/subscriptions/')


'''
Function below is taken
from https://testdriven.io/blog/django-stripe-subscriptions/
'''


@login_required
def success(request):
    messages.success(request, 'Your subscription was created successfully')
    return render(request, 'subscriptions/success.html')


'''
Function below is taken
from https://testdriven.io/blog/django-stripe-subscriptions/
'''


@login_required
def cancel(request):
    messages.success(request, 'Your subscription was aborted')
    return render(request, 'subscriptions/cancel.html')


'''
Function below is taken
from https://testdriven.io/blog/django-stripe-subscriptions/
'''


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET_SUB
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, wh_secret)
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        # Invalid signature
        return HttpResponse(status=400)
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        # Fetch all the required data from session
        client_reference_id = session.get('client_reference_id')
        stripe_customer_id = session.get('customer')
        stripe_subscription_id = session.get('subscription')
        # Get the user and create a new StripeCustomer
        user = User.objects.get(id=client_reference_id)
        StripeCustomer.objects.create(
            user=user,
            stripeCustomerId=stripe_customer_id,
            stripeSubscriptionId=stripe_subscription_id,
        )
    return HttpResponse(status=200)
