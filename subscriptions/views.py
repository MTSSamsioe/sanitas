from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
import stripe
import djstripe

import json
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from .models import StripeCustomer
from djstripe.models import Product, Plan, Subscription
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from subscriptions.models import StripeCustomer
from django.contrib import messages


from subscriptions.webhook_handler import StripeWH_Handler

@login_required
def stripe_subscriptions(request):
    """ A view to show all stripe gym subscriptions"""
    plans = Plan.objects.all()
    
    try:
        # Retrieve the subscription & product
        stripe_customer = StripeCustomer.objects.get(user=request.user)
        stripe.api_key = settings.STRIPE_SECRET_KEY
        subscription = stripe.Subscription.retrieve(stripe_customer.stripeSubscriptionId)
        product = stripe.Product.retrieve(subscription.plan.product)
        context = {
            'plans': plans,
            'subscription': subscription,
            'product': product,
        } 
        return render(request, 'subscriptions/stripe_subscriptions.html', context)

    except:
        
        context = {
            'plans': plans,
            
        } 
        

    return render(request, 'subscriptions/stripe_subscriptions.html', context)




@csrf_exempt
def cancel_sub(request):
    if request.user.is_authenticated:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
        try:
            subscription = StripeCustomer.objects.values_list('stripeSubscriptionId')[0][0]
            stripe.Subscription.delete(subscription,)
            messages.success(request, 'Your subscription is canceled')
        except:
            
            messages.warning(request, 'Unable to cancel subscription from stripe, please try again')
            return redirect('/')
        try:
            user = request.user    
            subscription_django = StripeCustomer.objects.filter(user=user)
            subscription_django.delete()
            messages.success(request, 'Your subscription is deleted from database')
        except:
            messages.warning(request, 'Unable to cancel subscription from database, please try again')
            return redirect('/')
        return redirect('/')
        
    else:
        return redirect('/accounts/login/')

@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        print(JsonResponse(stripe_config, safe=False))
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    
    if request.method == 'GET':
        domain_url = 'https://8000-mtssamsioe-sanitas-4vmeom2cqnk.ws-eu86.gitpod.io/subscriptions/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        
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

@login_required
def success(request):
    return render(request, 'subscriptions/success.html')


@login_required
def cancel(request):
    return render(request, 'subscriptions/cancel.html')


@csrf_exempt
def stripe_webhook(request):
    
    stripe.api_key = settings.STRIPE_SECRET_KEY
    wh_secret = settings.STRIPE_WH_SECRET_SUB
    
    

    payload = request.body
    
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
        
    except ValueError as e:
        # Invalid payload
        print(e)
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        print(e)
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed': #payment_intent.succeeded
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
        
        print(user.username + ' just subscribed.')

    return HttpResponse(status=200)