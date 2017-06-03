from django import forms
from django.contrib.auth.forms import UserCreationForm

class SubscriberForm(UserCreationForm):
	email = forms.EmailField(
		required=True, 
		wiget=forms.TextInput(attrs={'class':'inner'})
		)
	username = forms.CharField(
		wiget=forms.TextInput(attrs={'class':'inner'})
		)
	password1 = forms.CharField(
		wiget=forms.TextInput(attrs={'class':'inner', 'type': 'password'})
		)
	password2 = forms.CharField(
		wiget=forms.TextInput(attrs={'class':'inner', 'type': 'password'})
		)

    # def clean_username(self):
    # try:
    #     user = User.objects.get(username__iexact=self.cleaned_data['username'])
    # except User.DoesNotExist:
    #     return self.cleaned_data['username']
    # raise forms.ValidationError(_("The username already exists. Please try another one."))

    # def clean(self):
    #     if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
    #         if self.cleaned_data['password1'] != self.cleaned_data['password2']:
    #             raise forms.ValidationError(_("The two password fields did not match."))
    #     return self.cleaned_data
