from django.forms import ModelForm
from django import forms
from .models import Feedback


# Form used as the input for the search bar
class Search(forms.Form):
    search = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Eg. PSYC 100A', 'class': 'input_form'}))
    school = forms.ChoiceField(choices=[('UVic', 'University of Victoria'), ('UBC', 'University of British Columbia')], widget=forms.Select(attrs={'class': 'input_form_school'}))


# Form used to create a posting
class PostCreate(forms.Form):
    isbn = forms.CharField(max_length=13, min_length=13, required=True)
    CHOICES = (('New', 'New'), ('Like New', 'Like New'), ('Used', 'Used'), ('Usable', 'Usable'))
    price = forms.DecimalField(max_digits=5, decimal_places=2, error_messages={'Invalid': 'Price must be of a max of 5 numbers', 'required': 'A price is required to post.'})
    condition = forms.ChoiceField(choices=CHOICES)
    image = forms.ImageField(required=False)
    comments = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'class': 'postcomment'}), required=False)


# The contact form is used to save information in the feedback model
class Contact(ModelForm):
    class Meta:
        model = Feedback
        fields = ('email', 'subject', 'content')
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'feedback'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'feedback'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'feedbackcontent'}), required=True, label="Feedback")
