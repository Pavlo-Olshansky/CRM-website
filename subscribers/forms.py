from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import Subscriber

 
class AddressMixin(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ('address_one', 'address_two', 'city', 'state',)
        widgets = {
            'address_one': forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='Karadzic 8')),
            'address_two': forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='Karadzic 8a')),
            'city': forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='New York')),
            'state': forms.TextInput(attrs=dict(required=True, max_length=30, placeholder='NY')),
        }


class SubscriberForm(AddressMixin, UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30, placeholder='Pavlo')), label=_("First name"))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30, placeholder='Olshansky')), label=_("Last name"))

    email = forms.EmailField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30, placeholder='my_email@gmail.com')), label=_("Email address"))
    
    username = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30, placeholder='Awersome_name')), label=_("Username"), error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False, placeholder='8 character min')), label=_("Password"))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False, placeholder='Rewrite the pass')), label=_("Password (again)"))
