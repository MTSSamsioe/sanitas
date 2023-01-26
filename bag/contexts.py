def bag_products(request):
    bag_items = []
    total = 0
    product_count = 0



    cotext = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }
    return context