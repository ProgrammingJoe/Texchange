from bs4 import BeautifulSoup
from collections import namedtuple

import os
from django.core.management.base import BaseCommand, CommandError
from textchange.models import Textbook


class Command(BaseCommand):

    def cleanstr(self, str):
        str = str.replace('\n','')
        str = str.replace(' ','')
        return str

    def findbook(self, x):
        tag = x.find("b")
        book = tag.string
        return book

    def findauthor(self, x):
        tag = x.find("span", { "class" : "author"})
        author = tag.string
        author = self.cleanstr(author)
        author = author.replace("Author:", "")
        return author

    def findcourse(self, x):
        parent1 = x.parent
        parent2 = parent1.parent
        parent3 = parent2.parent
        info = parent3.find("div", { "class" : "row course-info"})
        coursetag = info.find('span')
        course = coursetag.string
        course = self.cleanstr(course)
        return course

    def findisbn(self, x):
        secondrow = x.findAll("div", { "class" : "row"})[1]
        link = secondrow.find('a')
        isbn = link.string
        isbn = self.cleanstr(isbn)
        return isbn

    def handle(self, *args, **options):
        print(os.listdir("."))
        soup = BeautifulSoup(open("bookstore.html"), "html.parser")
        books = soup.findAll("div", { "class" : "textbook-item"})
        bookmodels = []
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
            new = Textbook(textbook_name = dic['book'], class_name = dic['course'], author = dic['author'], isbn = dic['isbn'])
            new.save()
