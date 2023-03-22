
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

        labels = {
                
                'preset_full_name': 'Full name',
                'preset_email': 'Email',
                'preset_adress': 'Address',
                'preset_post_code': 'Post code',
                'preset_city': 'City',
        }
    
    def __init__(self, *args, **kwargs):
        """
        Add placeholders 
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'preset_full_name': 'Full Name',
            'preset_email': 'Email Address',
            'preset_adress': 'Street Address',
            'preset_post_code': 'Post Code',
            'preset_city': 'City',
            
        }

     