from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Products
from djstripe.models import Product

def bag_products(request):
    
    # bag for other products
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    # Bag for subscriptions 
    bag_items_subs = []
    total_subs = 0
    product_count_subs = 0
    bag_subs = request.session.get('bag_subs', {})

    
    for item_id, quantity in bag.items():
        print(item_id)
        if len(item_id) < 3:

            product = get_object_or_404(Products, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            bag_items.append ({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        


    
    for item_id, quantity in bag_subs.items():
        if len(item_id) > 3:
            product = get_object_or_404(Product, id=item_id)
            total += quantity * round(product.metadata["price"], 2)
            product_count_subs += quantity
            bag_items_subs.append ({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })


    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'bag_items_subs': bag_items_subs,
        'total_subs': total_subs,
        'product_count_subs': product_count_subs,
    }
    return context