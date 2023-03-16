from django import forms
from .models import Appointments

import datetime
from django.utils import timezone

from django.forms import ValidationError

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