
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from django import forms

from .models import User, Posting

class UserCreate(UserCreationForm):
	username = forms.CharField()
	password1 = forms.CharField()
	password2 = forms.CharField()
	email = forms.EmailField()
