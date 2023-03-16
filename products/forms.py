from django import forms
from .models import Appointments
from checkout.models import Order_item
from django.forms import ValidationError

from django.contrib.auth.models import User

# time packages
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime, timedelta
from django.utils import timezone
import pytz


class AppointmentsForm(forms.ModelForm):

    class Meta:

        model = Appointments
        fields = ['date_time']

        widgets = {
            'date_time': forms.DateTimeInput(attrs={
                    'class': 'form-control', 'type': 'datetime-local'}),
        }

        labels = {
                
                'date_time': 'Pick a date',
        }
    def __init__(self, *args, **kwargs):
         
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        # if user:
        # if Appointment_amount > purchased_hours:
        # raise ValidationError('testing')
        print('Slut på init')

    def clean_date_time(self, *args, **kwargs):
        date_time = self.cleaned_data.get('date_time')
        # Validation not to reserv a time before current time plus one hour
        
        if not date_time >= timezone.now() + timedelta(minutes=60):
            raise ValidationError('Pick a time at least 1 hour after current time')
        
        # Validation to prevent making appoint ment with to few purchased hours
        user = self.user
        purchased_hours = sum(i[0] for i in Order_item.objects.filter(user=user).values_list('quantity'))
        Appointment_amount = len(Appointments.objects.filter(user=user).values_list())
        print(purchased_hours)
        print(Appointment_amount)
        print(user)
        if user:
            if Appointment_amount > purchased_hours:
                raise ValidationError('No availeble sessions')

        return date_time
   
    

    
        