from bs4 import BeautifulSoup
from collections import namedtuple

import os, sys
sys.path.append("C:\\Users\\Joe Czepil\\Documents\\exchange\\Texchange")
os.environ["DJANGO_SETTINGS_MODULE"] = "exchange.settings"
from textchange.models import Textbook

soup = BeautifulSoup(open("bookstore.html"))

books = soup.findAll("div", { "class" : "textbook-item"})

def cleanstr(str):
    str = str.replace('\n','')
    str = str.replace(' ','')
    return str

def findbook(x):
    tag = x.find("b")
    book = tag.string
    return book

def findauthor(x):
    tag = x.find("span", { "class" : "author"})
    author = tag.string
    author = cleanstr(author)
    author = author.replace("Author:", "")
    return author

def findcourse(x):
    parent1 = x.parent
    parent2 = parent1.parent
    parent3 = parent2.parent
    info = parent3.find("div", { "class" : "row course-info"})
    coursetag = info.find('span')
    course = coursetag.string
    course = cleanstr(course)
    return course

def findisbn(x):
    secondrow = x.findAll("div", { "class" : "row"})[1]
    link = secondrow.find('a')
    isbn =  link.string
    isbn = cleanstr(isbn)
    return isbn

def main():
    bookmodels = []
    for x in books:
        book = findbook(x)
        author = findauthor(x)
        course = findcourse(x)
        isbn = findisbn(x)
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

main()
