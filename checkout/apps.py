
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'
    # Code below is taken from Code institute project lessons Boutique ado

    def ready(self):
        import checkout.signals
