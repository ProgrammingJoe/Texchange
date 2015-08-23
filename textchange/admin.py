from django.contrib import admin

# Register your models here.

from .models import Textbook, Posting, Wishlist

class Textbook_table(admin.ModelAdmin):
	fields = ['textbook_name', 'class_name', 'author', 'isbn', 'wishlist_count', 'listing_count']
	list_display = ('textbook_name', 'class_name', 'author', 'isbn', 'wishlist_count', 'listing_count')

class Wishlist_table(admin.ModelAdmin):
	fields = ['textbook', 'user', 'wish_date']
	list_display = ('textbook', 'user', 'wish_date')

class Posting_table(admin.ModelAdmin):
	fields = ['textbook', 'condition', 'price', 'user', 'image', 'post_date']
	list_display = ('textbook', 'condition', 'price', 'user', 'image', 'post_date')

admin.site.register(Textbook, Textbook_table)
admin.site.register(Wishlist, Wishlist_table)
admin.site.register(Posting, Posting_table)
