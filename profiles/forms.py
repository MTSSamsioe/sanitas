from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
    
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

     