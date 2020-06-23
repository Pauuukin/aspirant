from django import forms
from django.forms import SelectDateWidget
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class ManufacturerAddForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ('name', 'country')

    def __init__(self, *args, **kwargs):
        """Переопределяем метод init для формы, чтобы задать нужные классы"""
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control mt-2 mb-3'


