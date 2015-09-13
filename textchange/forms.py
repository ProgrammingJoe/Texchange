
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from django import forms

from .models import MyUser, Posting

# Form used to create a user
class UserCreate(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'password1', 'password2', 'email', 'facebook')
		widgets = {
		'password1': forms.PasswordInput(),
		'password2': forms.PasswordInput(),
		}
	username = forms.CharField()
	password1 = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)
	email = forms.EmailField(widget = forms.EmailInput)
	facebook = forms.CharField()


# Form used as the input for the search bar
class Search(forms.Form):
	search = forms.CharField(required = False)

# Form used to create a posting
class PostCreate(forms.Form):
	CHOICES = (('New', 'New'), ('Like New', 'Like New'), ('Used', 'Used'), ('Usable', 'Usable'))
	price = forms.CharField(max_length = 200)
	condition = forms.ChoiceField(choices = CHOICES)
	image = forms.ImageField(required=False)
