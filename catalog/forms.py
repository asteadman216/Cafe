# forms.py

from django import forms
from .models import Coffee, Tea, Kids

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = ['drink_temp', 'drink_flavor', 'drink_size', 'drink_type']

class TeaForm(forms.ModelForm):
    class Meta:
        model = Tea
        fields = ['drink_temp', 'drink_tea_flavor', 'drink_size', 'drink_tea_type']

class KidsForm(forms.ModelForm):
    class Meta:
        model = Kids
        fields = ['drink_temp', 'drink_kids_choices', 'drink_kids_flavor_choices', 'drink_size']