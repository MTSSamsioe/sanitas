'''
Structure, logic and class name is taken from boutique ado walkthrough project
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
250e2c2b8e43cccb56b4721cd8a8bd4de6686546/profiles/views.py
'''
from django.shortcuts import (render,
                              get_object_or_404,
                              reverse, redirect,
                              HttpResponseRedirect)
from .models import Profile
from checkout.models import Order_item, Order
from .forms import ProfileForm
from django.contrib import messages
from subscriptions.models import StripeCustomer
import stripe
from django.conf import settings


def profile(request):
    """
    Show users profiles
    """
    if request.user.is_authenticated:
        profile = get_object_or_404(Profile, user=request.user)

        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile is updated')
            else:
                messages.error(request, 'Something went wrong  \
                               please try again')
        else:
            form = ProfileForm(instance=profile)

        orders = profile.orders.all()
        context = {
            'form': form,
            'orders': orders,
        }

        return render(request, 'profiles/profile.html', context)
    else:
        messages.error(request, 'You must be logged  in to see user  profile. \
                       Please log in or create an account.')
        return redirect('/accounts/login/')
