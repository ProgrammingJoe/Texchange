from django.forms import ModelForm
from django import forms
from .models import Feedback


# Form used as the input for the search bar
class Search(forms.Form):
    search = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'input_form'}))
    CHOICES = (('UVic', 'University of Victoria'), ('-', 'More Schools Soon'))
    school = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.Select(attrs={'class': 'input_form_school'}))


# Form used to create a posting
class PostCreate(forms.Form):
    ISBN = forms.CharField(min_length=13, label="ISBN", required=True, widget=forms.TextInput(attrs={'class': 'add_posting_field'}))
    SCHOOLS = (('UVic', 'University of Victoria'), ('-', 'More Schools Soon'))
    school = forms.ChoiceField(choices=SCHOOLS, widget=forms.Select(attrs={'class': 'add_posting_field'}))
    CHOICES = (('', 'Condition'), ('New', 'New'), ('Like New', 'Like New'), ('Used', 'Used'), ('Usable', 'Usable'))
    price = forms.DecimalField(max_digits=5, decimal_places=2, widget=forms.TextInput(attrs={'class': 'add_posting_field'}), error_messages={'Invalid': 'Price must be of a max of 5 numbers', 'required': 'A price is required to post.'})
    condition = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'add_posting_field'}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'add_posting_image_field'}))
    comments = forms.CharField(max_length=50, widget=forms.Textarea(attrs={'class': 'add_posting_comments_field'}), required=False)


# The contact form is used to save information in the feedback model
class Contact(ModelForm):
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'subject', 'content')
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'feedback_field'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'feedback_field'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'feedback_field'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'feedback_textarea'}), required=True, label="Feedback")
