from bs4 import BeautifulSoup
import urllib2
from django.core.management.base import BaseCommand
from textchange.models import Textbook
import re
import time
import os


class Command(BaseCommand):
    def bookstoreprice(self, soup):
        new = "0"
        used = "0"
        prices = soup.find("div", {"class": "textbook-item"})
        prices2 = prices.findAll("span", {"class": "right"})
        for y in prices2:
            if y is not None:
                if "Used" in y.string:
                    used = y.string
                elif "New" in y.string:
                    new = y.string
            else:
                return(0, 0)
        new = new.replace(' ', '')
        a = re.search('[0-9]+\.[0-9][0-9]', new)
        if a:
            new = a.group(0)
        used = used.replace(' ', '')
        b = re.search('[0-9]+\.[0-9][0-9]', used)
        if b:
            used = b.group(0)
        new = float(new)
        used = float(used)
        return(new, used)

    def abeprice(self, soup):
        prices = soup.findAll("div", {"class": "cf result"})
        total = 0
        count = 0
        for x in prices:
            test = x.find("div", {"class": "international-edition"})
            if test is None:
                prices2 = x.find("div", {"class": "result-pricing col-xs-4"})
                startprice = prices2.find("div", {"class": "item-price"})
                shipprice = prices2.find("div", {"class": "shipping"})
                startprice = startprice.find("span")
                shipprice = shipprice.find("span")
                startprice = startprice.string[4:]
                shipprice = shipprice.string[4:]
                if shipprice == "":
                    total += float(startprice)
                else:
                    total += float(startprice) + float(shipprice)
                count += 1
                break
        if count == 0:
            return 99999
        else:
            return total/count

    # Main function to call all the methods
    def handle(self, *args, **options):
        abebase_one = "http://www.abebooks.com/servlet/SearchResults?isbn="
        abebase_two = "&sortby=2"
        uvicbase = "https://www.uvicbookstore.ca/text/book/"

        showmethemoney = []

        textbooks = Textbook.objects.filter(semester="SPRING2016").distinct('isbn')
        count = 0
        for book in textbooks:
            # time.sleep(4)
            if count % 25 == 0:
                print(count)
            os.environ['http_proxy'] = ''
            abelink = urllib2.urlopen(abebase_one + book.isbn + abebase_two)
            abepage = abelink.read()
            abelink.close()
            uviclink = urllib2.urlopen(uvicbase + book.isbn)
            uvicpage = uviclink.read()
            uviclink.close()
            abesoup = BeautifulSoup(abepage, "html.parser")
            uvicsoup = BeautifulSoup(uvicpage, "html.parser")
            price = self.bookstoreprice(uvicsoup)
            avgprice = self.abeprice(abesoup)
            if(avgprice != 99999 and price[1] != 0 and price[0] != 0):
                showmethemoney.append((book.isbn, price[1]-avgprice, price[0]-avgprice))
            if count == 300:
                break
            count += 1
        showmethemoney = sorted(showmethemoney, key=lambda x: -x[1])
        print("===================================")
        print("|     ISBN      || Used  ||  New  |")
        print("|===============||=======||=======|")
        for book in showmethemoney:
            print("| {0:s} || {1:5.2f} || {2:5.2f} |".format(book[0], book[1], book[2]))
        print("===================================")
