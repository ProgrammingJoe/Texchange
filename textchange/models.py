from django.db import models

# Create your models here.
"""
from django.contrib.auth.models import User	

class Textbook(models.Model):
	textbook_name = models.CharField(max_length = 200, blank=True)
	class_name = models.CharField(max_length = 200, blank=True)
	author = models.CharField(max_length = 200, blank=True)
	isbn = models.CharField(max_length = 200, primary_key=True,blank=True)
	wishlist_count = models.CharField(max_length = 200)
	listing_count = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.textbook_name
	
class Posting(models.Model):
	textbook = models.ForeignKey(Textbook)
	condition = models.CharField(max_length = 200, blank=True)
	price = models.CharField(max_length = 200, null=True)
	user = models.ForeignKey(User)
	post_date = models.DateTimeField('date_posted', blank=True)
	
	def __str__(self):
		return self.textbook
		
	def was_posted_recently(self):
		return self.post_date >= timezone.now() - datetime.timedelta(days=1)
	was_posted_recently.admin_order_field = 'post_date'
	was_posted_recently.boolean = True
	was_posted_recently.short_description = 'Posted recently'
	
class Wishlist(models.Model):
	textbook = models.ForeignKey(Textbook)
	user = models.ForeignKey(User)
	wish_date = models.DateTimeField('date_wish', blank=True)
	
	def __str__(self):
		return self.textbook
		
	def was_wished_recently(self):
		return self.wish_date >= timezone.now() - datetime.timedelta(days=1)
	was_wished_recently.admin_order_field = 'date_wish'
	was_wished_recently.boolean = True
	was_wished_recently.short_description = 'Wished recently'
"""