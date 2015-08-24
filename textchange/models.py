from django.db import models

# Create your models here.

from django.contrib.auth.models import User

# 770 3333 446

class Textbook(models.Model):
	textbook_name = models.CharField(max_length = 200)
	class_name = models.CharField(max_length = 200)
	author = models.CharField(max_length = 200)
	isbn = models.CharField(max_length = 200, primary_key=True)
	@property
	def NumWishes(self):
		return self.wishlist_set.count()
	@property
  	def NumPosts(self):
		return self.posting_set.count()
	@property
  	def DemSup(self):
		if (self.posting_set.count() != 0):
			showmethemoney = float((self.wishlist_set.count()))/(self.posting_set.count())
		else:
			showmethemoney = -1
		return showmethemoney

	def __str__(self):
		return self.textbook_name

class Posting(models.Model):
	textbook = models.ForeignKey(Textbook)
	condition = models.CharField(max_length = 200)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to='/home/joe/documents/texchange/media/postings/', default="../../static/textchange/nophoto.jpg")
	post_date = models.DateTimeField('date_posted')

	def __str__(self):
		return str(self.textbook)

	def was_posted_recently(self):
		return self.post_date >= timezone.now() - datetime.timedelta(days=1)
	was_posted_recently.admin_order_field = 'post_date'
	was_posted_recently.boolean = True
	was_posted_recently.short_description = 'Posted recently'

class Wishlist(models.Model):
	textbook = models.ForeignKey(Textbook)
	user = models.ForeignKey(User)
	wish_date = models.DateTimeField('date_wish')

	def __str__(self):
		return str(self.textbook)

	def was_wished_recently(self):
		return self.wish_date >= timezone.now() - datetime.timedelta(days=1)
	was_wished_recently.admin_order_field = 'date_wish'
	was_wished_recently.boolean = True
	was_wished_recently.short_description = 'Wished recently'
