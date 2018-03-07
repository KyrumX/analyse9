from django import forms

from requestapp.collection.static import choices


class BasicDetailsForm(forms.Form):
    name = forms.CharField(required=True, max_length=100)
    address = forms.CharField(required=True, max_length=100)

class ColorForm(forms.Form):
    color = forms.ChoiceField(choices=choices, required=True)