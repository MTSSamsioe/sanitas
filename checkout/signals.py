'''
All code below is taken from Code institute project lessons Boutique ado
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/signals.py

'''

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Order_item


@receiver(post_save, sender=Order_item)
def update_on_save(sender, instance, created, **kwargs):
    """Update order total on lineitem update/create"""

    instance.order.new_total()


@receiver(post_delete, sender=Order_item)
def update_on_delete(sender, instance, **kwargs):
    """Update order total on lineitem delete"""

    instance.order.new_total()
