from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

def view_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'bag/bag.html')


def add_bag_item(request, item_id):
    """ A View that adds products to shopping bag"""

    quantity = int(request.POST.get('quantity'))
    bag_session = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')
    if item_id in list(bag_session.keys()):
        bag_session[item_id] += quantity
    else:
        bag_session[item_id] = quantity

    request.session['bag'] = bag_session
    

    return  redirect(redirect_url)


def update_bag(request, item_id):
    """ A View the updates products in shopping bag"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    
    bag = request.session.get('bag', {})

    
    
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


    
