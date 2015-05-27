
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from django import forms

from .models import User

class UserCreate(UserCreationForm):
	#class Meta(UserCreationForm.Meta):
	#model = User
	username = forms.CharField()
	password1 = forms.CharField()
	password2 = forms.CharField()
	email = forms.EmailField()

	"""def clean_username(self):
		username = self.cleaned_data["username"]
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError(self.error_messages['duplicate_username'])"""