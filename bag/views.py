'''
All of the strucutre, logic, functions and variable names are taken from
Code institute project
Boutique ado https://github.com/Code-Institute-Solutions/boutique_ado_v1/
blob/250e2c2b8e43cccb56b4721cd8a8bd4de6686546/bag/views.py
'''
from django.shortcuts import (render,
                              redirect, reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages
from products.models import Products
from django.contrib.auth.decorators import login_required


def view_bag(request):
    """ A view that renders the shopping bag """
    if request.user.is_authenticated:
        return render(request, 'bag/bag.html')
    else:
        messages.error(request, 'You must be logged in to see shopping bag. \
                        Please log in or create an account.')
        return redirect('/accounts/login/')


def add_bag_item(request, item_id):
    """ A View that adds products to shopping bag"""
    redirect_url = request.POST.get('redirect_url')

    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        bag_session = request.session.get('bag', {})

        if item_id in list(bag_session.keys()):
            bag_session[item_id] += quantity
            messages.success(request, f'Updated {product.friendly_name} \
             quantity to {bag_session[item_id]}')

        else:
            bag_session[item_id] = quantity
            messages.success(request, f'Added {product.friendly_name} to your \
                            bag')

        request.session['bag'] = bag_session
        return redirect(redirect_url)
    else:
        messages.error(request, 'You must be logged in to add to shopping bag \
                        please log in or create an account')
        return redirect('/accounts/login/')


def adjust_bag(request, item_id):
    """ A View the updates products in shopping bag"""
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    bag_session = request.session.get('bag', {})

    if quantity > 0:
        bag_session[item_id] = quantity
        messages.success(request, f'Updated {product.friendly_name}  \
                        quantity to {bag_session[item_id]}')
    else:
        bag_session.pop(item_id)
        messages.success(request, f'Removed {product.friendly_name} \
                        from your bag')
    request.session['bag'] = bag_session
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ A View that removes products from shopping bag"""

    try:
        product = get_object_or_404(Products, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.friendly_name} \
                        from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item from bag: {e}')
        return HttpResponse(status=500)
