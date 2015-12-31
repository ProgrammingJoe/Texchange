from django.contrib import admin
from django.forms import Textarea
from django.db import models
# Register your models here.

from .models import Textbook, Posting, Wishlist, Feedback


# Fields is the list of elements in the table
# List_display is the list of attributes and/or properties viewable on admin site
class Textbook_table(admin.ModelAdmin):
    fields = ['textbook_name', 'class_name', 'author', 'isbn', 'semester']
    list_display = ('textbook_name', 'class_name', 'author', 'isbn', 'semester', 'NumPosts', 'NumWishes', 'DemSup')


class Wishlist_table(admin.ModelAdmin):
    fields = ['textbook', 'user', 'wish_date']
    list_display = ('textbook', 'user', 'wish_date')


class Posting_table(admin.ModelAdmin):
    fields = ['textbook', 'condition', 'price', 'user', 'image', 'comments', 'post_date']
    list_display = ('textbook', 'condition', 'price', 'user', 'image', 'comments', 'post_date')


# Formfield is set so long message
class Feedback_table(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': Textarea(attrs={'rows': 5, 'col': 40})},
    }
    fields = ['email', 'subject', 'content', 'user']
    list_display = ('email', 'subject', 'content', 'user')

# Adds the models to the admin site
admin.site.register(Textbook, Textbook_table)
admin.site.register(Wishlist, Wishlist_table)
admin.site.register(Posting, Posting_table)
admin.site.register(Feedback, Feedback_table)
