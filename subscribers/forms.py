from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import Subscriber  


class AddressMixin(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('address_one', 'address_two', 'city', 'state',)
        widgets = {
            'address_one': forms.TextInput(attrs={'class':'form-control'}),
            'address_two': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
        }  


class SubscriberForm(AddressMixin, UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("First name"))
    
    last_name = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Last name"))

    email = forms.EmailField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Email address"))
    
    username = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
