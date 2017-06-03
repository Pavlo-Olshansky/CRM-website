from django import forms
from django.contrib.auth.forms import UserCreationForm

class ContactForm(forms.ModelForm):
	search_query = forms.CharField(max_length=100)

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
