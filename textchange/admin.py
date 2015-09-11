from django.contrib import admin

# Register your models here.

from .models import Textbook, Posting, Wishlist, MyUser

# Fields is the list of elements in the table
# List_display is the list of attributes and/or properties viewable on the admin site
class Textbook_table(admin.ModelAdmin):
	fields = ['textbook_name', 'class_name', 'author', 'isbn']
	list_display = ('textbook_name', 'class_name', 'author', 'isbn', 'NumPosts', 'NumWishes', 'DemSup')

class Wishlist_table(admin.ModelAdmin):
	fields = ['textbook', 'user', 'wish_date']
	list_display = ('textbook', 'user', 'wish_date')

class Posting_table(admin.ModelAdmin):
	fields = ['textbook', 'condition', 'price', 'user', 'image', 'post_date']
	list_display = ('textbook', 'condition', 'price', 'user', 'image', 'post_date')

class MyUser_table(admin.ModelAdmin):
	fields = ['user', 'facebook']
	list_display = ('user', 'facebook')

# Adds the models to the admin site
admin.site.register(Textbook, Textbook_table)
admin.site.register(Wishlist, Wishlist_table)
admin.site.register(Posting, Posting_table)
admin.site.register(MyUser, MyUser_table)
