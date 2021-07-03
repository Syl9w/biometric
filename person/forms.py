from django import forms
from django.forms import fields
from .models import Person

class IINForm(forms.Form):
    iin = forms.CharField(max_length=12)
    