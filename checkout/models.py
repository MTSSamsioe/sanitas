import uuid


from django.db import models
from django.db.models import Sum

from django.conf import settings

from products.models import Products


class Order(models.Model):
    
    order_number = models.CharField(max_length= 50, null=False, editable=False)
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    adress = models.CharField(max_length=100, null=False, blank=False)
    post_code = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _make_order_number(self):
        """ Make a random and unique ordernumber using uuid"""
        return uuid.uuid4().hex.upper()

    def new_total(self):

        """ Update total each time a order item is added """
        self.total = self.Order_item.aggregate(Sum('order_item_total'))['order_item_total__sum']
        self.save()

    def save(sself, *args, **kwargs):

        """ Overide save method to set the order number """
        if not self.order_number: 
            self.order_number = self._make_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class Order_item(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name= 'orderitems')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False, editable=False)
    order_item_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(sself, *args, **kwargs):

        """ Overide save method to set the order number """
        self.order_item_total = self.products.price * self.quantity
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.products.name} on order {self.order.order_number}'