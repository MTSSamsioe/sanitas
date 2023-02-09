from django.shortcuts import render, redirect
import stripe
import json
from django.http import JsonResponse
from .models import Membership
from djstripe.models import Product, Plan
from django.contrib.auth.decorators import login_required

def stripe_subscriptions(request):
    """ A view to show all stripe gym subscriptions"""
    plans = Plan.objects.all()
    subscriptions = Product.objects.all()
    context = {
        'plans': plans,
        'subscriptions': subscriptions,
        
    }

    return render(request, 'subscriptions/stripe_subscriptions.html', context)

@login_required
def checkout_sub(request):
  products = Product.objects.all()

  context = {
    "products": products,
  }

  return render(request,"subscriptions/checkout_sub.html",context)

@login_required
def create_sub(request):
    if request.method == 'POST':
        # Reads application/json and returns a response
        data = json.loads(request.body)
        payment_method = data['payment_method']
        stripe.api_key = djstripe.settings.STRIPE_SECRET_KEY

        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)


        try:
            # This creates a new Customer and attaches the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )

            djstripe_customer = djstripe.models.Customer.sync_from_stripe_data(customer)
            request.Membership.customer = djstripe_customer # ändrad ifrån request.user.customer till 
          

            # At this point, associate the ID of the Customer object with your
            # own internal representation of a customer, if you have one.
            # print(customer)

            # Subscribe the user to the subscription created
            subscription = stripe.Subscription.create(
                customer= request.Membership.user,   # ändrad ifrån customer.id, 
                items=[
                    {
                        "price": data["price_id"],
                    },
                ],
                expand=["latest_invoice.payment_intent"]
            )

            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

            request.Membership.subscription = djstripe_subscription
            request.Membership.save()

            return JsonResponse(subscription)
        except Exception as e:
            return JsonResponse({'error': (e.args[0])}, status =403)
    else:
      return HTTPresponse('requet method not allowed')


def complete(request):
  return render(request, "subscriptions/complete.html")