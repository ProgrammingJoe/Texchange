from bs4 import BeautifulSoup
import urllib2
from django.core.management.base import BaseCommand
from textchange.models import Textbook
import operator


class Command(BaseCommand):
    def bookstoreprice(self, soup):
        new = "0"
        used = "0"
        prices = soup.find("div", {"class": "textbook-item"})
        prices2 = prices.findAll("span", {"class": "right"})
        for y in prices2:
            if "Used" in y.string:
                used = y.string
            elif "New" in y.string:
                new = y.string
        new = new.replace(' ', '')
        new = new[6:]
        used = used.replace(' ', '')
        used = used[7:]
        return(new, used)

    def abeprice(self, soup):
        prices = soup.findAll("div", {"class": "cf result"})
        for x in prices:
            prices2 = x.find("div", {"class": "result-pricing col-xs-4"})
            startprice = prices2.find("div", {"class": "item-price"})
            shipprice = prices2.find("div", {"class": "shipping"})
            startprice = startprice.find("span")
            shipprice = shipprice.find("span")
            startprice = startprice.string
            shipprice = shipprice.string
            print("@@@@@@@@@@@@@@@@@")
            print(startprice)
            print(shipprice)
            # print(x)


    # Main function to call all the methods
    def handle(self, *args, **options):
        abebase_one = "http://www.abebooks.com/servlet/SearchResults?isbn="
        abebase_two = "&sortby=96&sts=t"
        uvicbase = "https://www.uvicbookstore.ca/text/book/"

        # textbooks = Textbook.objects.all().distinct('isbn')
        isbn = "9780321573513"
        # for book in textbooks:
        abepage = urllib2.urlopen(abebase_one + isbn + abebase_two).read()
        uvicpage = urllib2.urlopen(uvicbase + isbn)
        abesoup = BeautifulSoup(abepage)
        uvicsoup = BeautifulSoup(uvicpage)
        price1 = self.bookstoreprice(uvicsoup)
        price2 = self.abeprice(abesoup)
