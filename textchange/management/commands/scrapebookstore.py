from bs4 import BeautifulSoup
from collections import namedtuple

import os
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Q
from textchange.models import Textbook

# This command is used to scrape the UVicBookstore of their textbook information
# The html of the bookstore must be put into bookstore.html
# It can be called with 'python manage.py scrapebookstore.py'

class Command(BaseCommand):

    # Clean up garbage off the string before saving in the db
    def cleanstr(self, str):
        str = str.replace('\n','')
        str = str.replace(' ','')
        return str

    # Get the textbook name
    def findbook(self, x):
        tag = x.find("b")
        book = tag.string
        return book

    # Get the textbook author
    # Find all spans in x with class author
    def findauthor(self, x):
        tag = x.find("span", { "class" : "author"})
        author = str(tag)
        author = author[47:-8]
        author = self.cleanstr(author)
        author = author.replace("Author:", "")
        return author

    # Get the course name
    # Find all divs with class row course-info for the parentx3 of x
    def findcourse(self, x):
        parent1 = x.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        info = parent3.find("div", { "class" : "row course-info"})
        coursetag = info.find('span')
        course = coursetag.string
        course = self.cleanstr(course)
        return course

    # Get the isbn of the book
    # Get the first div with class row in x
    def findisbn(self, x):
        secondrow = x.findAll("a", { "class" : "skew"})[0]
        isbn = secondrow.string
        isbn = self.cleanstr(isbn)
        return isbn

    # Main function to call all the methods
    def handle(self, *args, **options):
        print(os.listdir("."))
        # Open up the bookstore.html into soup
        soup = BeautifulSoup(open("bookstore.html"), "html.parser")
        # Make a list of all textbooks divs and assign to books
        books = soup.findAll("div", { "class" : "textbook-item"})
        bookmodels = []
        # Loop through all books, find all information and save to the database
        for x in books:
            book = self.findbook(x)
            author = self.findauthor(x)
            course = self.findcourse(x)
            isbn = self.findisbn(x)
            object = {
                'book': book,
                'author': author,
                'course': course,
                'isbn': isbn,
            }
            bookmodels.append(object)

        for dic in bookmodels:
            ltextbook = Textbook.objects.filter(Q(isbn = dic['isbn']) & Q(class_name = dic['course']))
            if ltextbook:
                Textbook.objects.filter(Q(isbn = dic['isbn']) & Q(class_name = dic['course'])).update(semester = "SPRING2016")
            else:
                new = Textbook(textbook_name = dic['book'], class_name = dic['course'], author = dic['author'], isbn = dic['isbn'], semester = "SPRING2016")
                new.save()
