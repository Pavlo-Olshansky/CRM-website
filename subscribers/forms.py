from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class SubscriberForm(UserCreationForm):  # forms.Form
    email = forms.EmailField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Email address"))
    
    username = forms.CharField(widget=forms.TextInput(
        attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={'invalid': _("This value must contain only letters, numbers and underscores.")})

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))
