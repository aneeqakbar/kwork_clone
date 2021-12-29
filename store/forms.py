from django import forms
from django.core.exceptions import ValidationError
from .models import Gig, GigPackage

class CreateGigForm(forms.ModelForm):
    category = forms.CharField(max_length=150, required=True)

    class Meta:
        model = Gig
        fields = ['name', 'image', 'description']

class CreatePackageForm(forms.ModelForm):
    class Meta:
        model = GigPackage
        fields = ['price', 'package_description', 'delivery']
