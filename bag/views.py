from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Products
from djstripe.models import Product, Plan

def view_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'bag/bag.html')


def add_bag_item(request, item_id):
    """ A View that adds products to shopping bag"""
    redirect_url = request.POST.get('redirect_url')

    if request.user.is_authenticated:
        product = get_object_or_404(Products, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        bag_session = request.session.get('bag', {})
        
        if item_id in list(bag_session.keys()):
            bag_session[item_id] += quantity
            messages.success(request, f'Updated {product.friendly_name} quantity to {bag_session[item_id]}')
        else:
            bag_session[item_id] = quantity
            messages.success(request, f'Added {product.friendly_name} to your bag')

        request.session['bag'] = bag_session
        return redirect(redirect_url)
    else:
        messages.error(request, 'You must be logged in to add to shopping bag please log in or create an account')
        return redirect('/accounts/login/')


 ### STRIPE SUBSCRIPTION ###       
def add_subscription(request, item_id):
    """ A View that adds products to shopping bag"""
    redirect_url = request.POST.get('redirect_url')

    if request.user.is_authenticated:
        product = get_object_or_404(Plan, id=item_id)
        quantity = int(request.POST.get('quantity')) # ta bort
        bag_session = request.session.get('bag', {})
        
        if item_id in list(bag_session.keys()):
            messages.success(request, 'A subscription is alreadyin your bag, please remove before adding a new one')
        else:
            bag_session[item_id] = quantity
            messages.success(request, f'Added subscription to your bag')

        request.session['bag'] = bag_session
        
        return redirect(redirect_url)
    else:
        messages.error(request, 'You must be logged in to add to shopping bag please log in or create an account')
        return redirect('/accounts/login/')
#____________________________________________   



def adjust_bag(request, item_id):
    """ A View the updates products in shopping bag"""
    product = get_object_or_404(Products, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    
    bag_session = request.session.get('bag', {})

    if quantity > 0:
        bag_session[item_id] = quantity
        messages.success(request, f'Updated {product.friendly_name} quantity to {bag_session[item_id]}')
    else:
        bag_session.pop(item_id)
        messages.success(request, f'Removed {product.friendly_name} from your bag')
    request.session['bag'] = bag_session
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ A View that removes products from shopping bag"""
    if len(item_id) < 3:
        try:
            product = get_object_or_404(Products, pk=item_id)
            bag = request.session.get('bag', {})
            bag.pop(item_id)
            messages.success(request, f'Removed {product.friendly_name} from your bag')

            request.session['bag'] = bag
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, f'Error removing item from bag: {e}')
            return HttpResponse(status=500)
    if len(item_id) > 3:
        try:
            product = get_object_or_404(Plan, id=item_id)
            bag = request.session.get('bag', {})
            bag.pop(item_id)
            messages.success(request, 'Removed subsciption from your bag')
            request.session['bag'] = bag
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(request, f'Error removing item from bag: {e}')
            return HttpResponse(status=500)