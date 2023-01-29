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