from bs4 import BeautifulSoup
import urllib2
from django.core.management.base import BaseCommand
from textchange.models import Textbook
import operator


class Command(BaseCommand):
    def bookstoreprice():
        print("one")

    def abeprice():
        print("two")

    # Main function to call all the methods
    def handle(self, *args, **options):
        abebase_one = "http://www.abebooks.com/servlet/SearchResults?isbn="
        abebase_two = "&sortby=96&sts=t"
        uvicbase = "https://www.uvicbookstore.ca/text/book/"

        comparison = {}

        textbooks = Textbook.object.values('isbn').distinct
        for book in textbooks:
            abepage = urllib2.urlopen(abebase_one + book.isbn + abebase_two).read()
            uvicpage = urllib2.urlopen(uvicbase + book.isbn)
            abesoup = BeautifulSoup(abepage)
            uvicsoup = BeautifulSoup(uvicpage)
            price1 = self.bookstoreprice(uvicsoup)
            price2 = self.abeprice(abesoup)
            if price1 and price2:
                comparison[book.isbn] = float(price1) - float(price2)

        sorted_prices = sorted(comparison.items(), key=operator.itemgetter(1))
        print(sorted_prices[:20])
