from django.contrib import admin
from subscriptions.models import StripeCustomer


class StripeCustomerAdmin(admin.ModelAdmin):

    fields = ('user', 'stripeCustomerId', 'stripeSubscriptionId'
              )

    list_display = ('user',
                    'stripeCustomerId', 'stripeSubscriptionId')


admin.site.register(StripeCustomer, StripeCustomerAdmin)
