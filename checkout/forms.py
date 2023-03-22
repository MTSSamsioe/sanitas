from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'adress', 'post_code', 'city')

        labels = {'adress': 'Adres',}
    
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

        #self.fields['full_name'].widget.attrs['autofocus'] = True
        
        #self.fields[field].widget.attrs['placeholder'] = placeholder
        #self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        #self.fields[field].label = False