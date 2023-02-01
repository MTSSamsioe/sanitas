from django.shortcuts import render, reverse, redirect
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_products

import stripe

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    if not bag:
        message.error(request,'There is nothing in your bag')
        return redirect(reverse('products'))
    
    current_bag = bag_products(request)
    total = current_bag['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, ('Stripe public key is missing. '
                                   ))


    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'checkout/checkout.html', context)
