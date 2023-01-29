from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404


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


def adjust_bag(request, item_id):
    """ A View the updates products in shopping bag"""

    quantity = int(request.POST.get('quantity'))
    
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        
    else:
        bag.pop(item_id)
    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ A View that removes products from shopping bag"""

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
            

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)