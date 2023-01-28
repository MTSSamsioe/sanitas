from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404

def view_bag(request):
    """ A view that renders the shopping bag """

    return render(request, 'bag/bag.html')


def add_bag_item(request, item_id):
    """ A View the adds products to shopping bag"""

    quantity = int(request.POST.get('quantity'))
    bag_session = request.session.get('bag', {})
    redirect_url = request.POST.get('redirect_url')
    if item_id in list(bag_session.keys()):
        bag_session[item_id] += quantity
    else:
        bag_session[item_id] = quantity

    request.session['bag'] = bag_session
    

    return  redirect(redirect_url)