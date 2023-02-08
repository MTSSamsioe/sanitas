from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Products
from djstripe.models import Product

def bag_products(request):
    
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    
    for item_id, quantity in bag.items():
        if isinstance(item_id, int):
            product = get_object_or_404(Products, pk=item_id)
            total += quantity * product.price
            product_count += quantity
            bag_items.append ({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, id=item_id)
            total += quantity * round(product.metadata["price"], 2)
            
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