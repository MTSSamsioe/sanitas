'''
Class name and method is taken from Boutique ado project
https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/
250e2c2b8e43cccb56b4721cd8a8bd4de6686546/checkout/forms.py
'''
from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'adress', 'post_code', 'city')

        labels = {'adress': 'Address', }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'adress': 'Street Address',
            'post_code': 'Post Code',
            'city': 'City',

        }
