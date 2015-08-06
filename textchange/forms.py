
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from django import forms

from .models import User, Posting

class UserCreate(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email', 'phone')
		widgets = {
		'password1': forms.PasswordInput(),
		'password2': forms.PasswordInput(),
		}
	username = forms.CharField()
	password1 = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)
	email = forms.EmailField()
	phone = forms.CharField()

class Search(forms.Form):
	search = forms.CharField(required = False)

class AddWishlist(forms.Form):
	pass
#
# class RemoveWishlist(forms.Form):
# 	pass
#
# class RemovePosting(forms.Form):
# 	pass
