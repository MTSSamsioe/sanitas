from django.shortcuts import render, reverse, redirect
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request,'There is nothing in your bag')
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51M8nSSBxdi5CQaAbFzfDVl6pXNeAZzmuCuOJ6ys8BQ0ror4gN6e5Mbkgb0up0St8AnNY3pqHkUJtpKEfi8hdbT5V00BG4WFEAY',
        'client_secret': 'sk_test_51M8nSSBxdi5CQaAbMR3c3A8xd4bNh8tf1o36IY6ITYSWIZ6wnGvIpj6AtgxktluvdbBspdiqgxhkeoiaJFBesvA400cePDFir5',
    }

    return render(request, 'checkout/checkout.html', context)
