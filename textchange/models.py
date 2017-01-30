from django.db import models
from django.contrib.auth.models import User
from auditlog.registry import auditlog
from auditlog.models import LogEntry


# Feedback model consists of feedback, a subject, and contact info
class Feedback(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    # Default user is Joe because I couldn't figure out how to remove this attribute (Bad practice :()
    user = models.ForeignKey(User, default=20)


# Textbook model with properties for determining supply and demand of textbooks
class Textbook(models.Model):
    textbook_name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200)
    semester = models.CharField(max_length=200, default="FALL2015")
    longschool = models.CharField(max_length=200, default="University of Victoria")
    shortschool = models.CharField(max_length=20, default="UVic")

    @property
    def NumPosts(self):
        return Posting.objects.filter(textbook__isbn=self.isbn).count()
        # return self.posting_set.count()

    @property
    def DemSup(self):
        if (self.posting_set.count() != 0):
            showmethemoney = float((self.wishlist_set.count()))/(self.posting_set.count())
        else:
            showmethemoney = 0
            return showmethemoney

# Instead of a pk field isbn and class_name together have to be unique
    class Meta:
        unique_together = ('isbn', 'class_name')

    def __str__(self):
        return self.textbook_name


# Posting model consisting of a textbook connected with a user
class Posting(models.Model):
    textbook = models.ForeignKey(Textbook, on_delete=models.CASCADE)
    condition = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='postingpics/%Y/%m/%d', default="/textchange/nophoto.png")
    post_date = models.DateTimeField('date_posted')
    comments = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.textbook)

    def was_posted_recently(self):
        return self.post_date >= timezone.now() - datetime.timedelta(days=1)
    was_posted_recently.admin_order_field = 'post_date'
    was_posted_recently.boolean = True
    was_posted_recently.short_description = 'Posted recently'


# LogEntry.objects.get_for_model(Posting).filter(action=2).count() to get number of deleted postings
auditlog.register(Posting)
