'''
All logic, function and variable names are taken from boutique ado
walkthrough project:
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/views.py
'''
from django.shortcuts import (render, reverse, redirect,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST

from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, Order_item
from products.models import Products

from bag.contexts import bag_products

from django.contrib.auth.models import User

from profiles.models import Profile
from profiles.forms import ProfileForm

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            finalized')
        return HttpResponse(content=e, status=400)


def checkout(request):
    '''View to process a purchase with stripe'''
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
                'full_name': request.POST['full_name'],
                'email': request.POST['email'],
                'post_code': request.POST['post_code'],
                'city': request.POST['city'],
                'adress': request.POST['adress'],
            }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save()

            for item_id, item_data in bag.items():

                product = Products.objects.get(id=item_id)
                order_line_item = Order_item(
                    user=request.user,
                    order=order,
                    product=product,
                    quantity=item_data,
                )
                order_line_item.save()
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form')
    else:
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, 'There is nothing in your bag')
            return redirect('/')

        current_bag = bag_products(request)
        total = current_bag['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        if request.user.is_authenticated:
            try:
                profile = Profile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.preset_full_name,
                    'email': profile.preset_email,
                    'post_code': profile.preset_post_code,
                    'city': profile.preset_city,
                    'adress': profile.preset_adress,
                })
            except Profile.DoesNotExist:
                order_form = OrderForm()
        else:
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


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    profile = Profile.objects.get(user=request.user)
    order.user_profile = profile
    order.save()

    # Save the users info
    if save_info:

        profile_data = {
            'preset_full_name': order.full_name,
            'preset_email': order.email,
            'preset_post_code': order.post_code,
            'preset_city': order.city,
            'preset_adress': order.adress,
        }
        user_profile_form = ProfileForm(profile_data, instance=profile)
        if user_profile_form.is_valid():
            user_profile_form.save()

    messages.success(request, f'Order was successful \
        Your order number is {order_number}.')

    if 'bag' in request.session:
        del request.session['bag']

    context = {
        'order': order,
    }

    return render(request, 'checkout/checkout_success.html', context)
