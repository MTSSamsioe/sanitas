# All of the strucutre, logic, function and variable names are taken from Code institute project lessons Boutique ado
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Products
def bag_products(request):
    
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    for item_id, quantity in bag.items():
        product = get_object_or_404(Products, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append ({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }
    return context