# forms.py

from django import forms
from .models import Coffee, Tea, Kids, CartItem

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

class CoffeeFilterForm(forms.Form):
    drink_type = forms.ChoiceField(choices=Coffee.DRINK_TYPE_CHOICES, required=False, label='Type')
    drink_temp = forms.ChoiceField(choices=Coffee.DRINK_TEMP_CHOICES, required=False, label='Temperature')
    drink_flavor = forms.ChoiceField(choices=Coffee.DRINK_FLAVOR_CHOICES, required=False, label='Flavor')
    drink_size = forms.ChoiceField(choices=Coffee.DRINK_SIZE_CHOICES, required=False, label='Size')

class TeaFilterForm(forms.Form):
    drink_type = forms.ChoiceField(choices=Tea.DRINK_TEA_CHOICES, required=False, label='Type')
    drink_temp = forms.ChoiceField(choices=Tea.DRINK_TEMP_CHOICES, required=False, label='Temperature')
    drink_flavor = forms.ChoiceField(choices=Tea.DRINK_TEA_SYRUP_CHOICES, required=False, label='Flavor')
    drink_size = forms.ChoiceField(choices=Tea.DRINK_SIZE_CHOICES, required=False, label='Size')

class KidsFilterForm(forms.Form):
    drink_type = forms.ChoiceField(choices=Kids.DRINK_KIDS_CHOICES, required=False, label='Type')
    drink_temp = forms.ChoiceField(choices=Kids.DRINK_TEMP_CHOICES, required=False, label='Temperature')
    drink_flavor = forms.ChoiceField(choices=Kids.DRINK_KIDS_FLAVOR_CHOICES, required=False, label='Flavor')
    drink_size = forms.ChoiceField(choices=Kids.DRINK_SIZE_CHOICES, required=False, label='Size')

class CartAddProductForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']