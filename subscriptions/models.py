from django.db import models
from django.contrib.auth.models import User
from djstripe.models import Customer, Subscription


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, null=True, blank=True, on_delete=models.SET_NULL)
    stripeCustomerId = models.CharField(max_length=255)
    stripeSubscriptionId = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username