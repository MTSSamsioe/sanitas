from django import forms
from .models import Appointments
from checkout.models import Order_item
from django.forms import ValidationError

from django.contrib.auth.models import User

# time packages
from datetime import datetime, timedelta
from django.utils import timezone


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

    def clean_date_time(self, *args, **kwargs):
        date_time = self.cleaned_data.get('date_time')
        date_time_end = date_time + timedelta(minutes=60)
        # Validation not to reserv a time before current time plus one hour

        if date_time <= timezone.now() + timedelta(minutes=60):
            raise ValidationError('Pick \
                                  a time at least 1 hour after current time')

        # Validation to prevent making appoint ment with to few purchased hours
        user = self.user
        purchased_hours = sum(i[0] for i in
                              Order_item.objects.filter(user=user)
                              .values_list('quantity'))
        appointment_amount = len(Appointments
                                 .objects.filter(user=user)
                                 .values_list())

        if user:
            if appointment_amount >= purchased_hours:
                raise ValidationError('No available personal \
                                    trainer sessions, please purchase more \
                                     and try again')

        ''' Validation to prevent making an appointment
         when there are already one appointment'''

        for tuple in (Appointments
                      .objects.filter(user=user).values_list('date_time')):
            for time in tuple:
                end_time = time + timedelta(minutes=60)

                if date_time >= time and date_time <= end_time:
                    raise ValidationError('You do already have an appointment \
                        at this time please pick another time')

        return date_time
