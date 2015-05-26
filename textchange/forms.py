"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm

from django import forms

from .models import User

class CreateForm(ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')

class TextbookForm(forms.Form):
	class Meta:
		model = User
		fields = ('username')
	seller_name = forms.CharField(label='seller_name', max_length=100)
"""	