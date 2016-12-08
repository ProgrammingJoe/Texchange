from django.contrib import admin
from django.forms import Textarea
from django.db import models
# Register your models here.

from .models import Textbook, Posting, Feedback
from auditlog.models import LogEntry


# Fields is the list of elements in the table
# List_display is the list of attributes and/or properties viewable on admin site
class Textbook_table(admin.ModelAdmin):
    fields = ['textbook_name', 'class_name', 'author', 'isbn', 'semester', 'longschool', 'shortschool']
    list_display = ('textbook_name', 'class_name', 'author', 'isbn', 'semester', 'longschool', 'shortschool', 'NumPosts', 'DemSup')


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


class Audit_table(admin.ModelAdmin):
    fields = ['action', 'actor', 'actor_id', 'additional_data', 'changes', 'content_type', 'content_type_id', 'id', 'object_id', 'object_pk', 'object_repr', 'remote_addr', 'timestamp']
    list_display = ('action', 'actor', 'actor_id', 'additional_data', 'changes', 'content_type', 'content_type_id', 'id', 'object_id', 'object_pk', 'object_repr', 'remote_addr', 'timestamp')

# Adds the models to the admin site
admin.site.register(Textbook, Textbook_table)
admin.site.register(Posting, Posting_table)
admin.site.register(Feedback, Feedback_table)
admin.site.register(LogEntry, Audit_table)
