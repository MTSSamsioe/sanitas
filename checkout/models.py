import uuid


from django.db import models
from django.db.models import Sum

from django.conf import settings

from products.models import Products
from profiles.models import Profile
from django.contrib.auth.models import User

class Order(models.Model):
    
    order_number = models.CharField(max_length=50, null=False, editable=False)
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, 
                                     null=True, related_name='orders')
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
        self.total = self.lineitems.aggregate(Sum('order_item_total'))['order_item_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):

        """ Overide save method to set the order number """
        if not self.order_number: 
            self.order_number = self._make_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class Order_item(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False, related_name='lineitems')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_item_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):

        """ Overide save method to set the order number """
        if self.product:
            self.order_item_total = self.product.price * self.quantity
            super().save(*args, **kwargs)
        # if self.plan:
        #    self.order_item_total = self.plan.amount * self.quantity
        #    super().save(*args, **kwargs)
    
    def __str__(self):

        if self.product:
            return f'{self.product.name} on order {self.order.order_number}'
        
        # if self.plan:
        #    return f'Plan on order {self.order.order_number}'