from django import forms
from django.forms import ModelForm

class NameForm(forms.Form):
    char_name = forms.CharField(max_length=100)
