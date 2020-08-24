from django import forms

import datetime

from .models import Pet, PetType
from django.forms.widgets import DateInput
# from django.forms.widgets import BootstrapDateTimePickerInput

class PetForm(forms.ModelForm):

    reg_date = forms.DateTimeField(required=True, widget=DateInput(attrs={'type': 'datetime-local'}),
                                     initial=format(datetime.date.today(), '%Y-%m-%d'),
                                     localize=True,)
    # reg_date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=BootstrapDateTimePickerInput()
    # )

    class Meta:
        model = Pet
        fields = '__all__'


class PetTypeForm(forms.ModelForm):
    class Meta:
        model = PetType
        fields = '__all__'

