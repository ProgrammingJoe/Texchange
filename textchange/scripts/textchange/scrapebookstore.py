from bs4 import BeautifulSoup
from collections import namedtuple

soup = BeautifulSoup(open("bookstore.html"))

books = soup.findAll("div", { "class" : "textbook-item"})

def cleanstr(str):
    str = str.replace('\n','')
    str = str.replace(' ','')
    return str

def findbook(x):
    tag = x.find("b")
    print("%s"% tag.string)

def findauthor(x):
    tag = x.find("span", { "class" : "author"})
    author = tag.string
    author = cleanstr(author)
    author = author.replace("Author:", "")
    print("%s"% author)

def findcourse(x):
    parent1 = x.parent
    parent2 = parent1.parent
    parent3 = parent2.parent
    info = parent3.find("div", { "class" : "row course-info"})
    coursetag = info.find('span')
    course = coursetag.string
    course = cleanstr(course)
    print("%s"% course)

def findisbn(x):
    secondrow = x.findAll("div", { "class" : "row"})[1]
    link = secondrow.find('a')
    isbn =  link.string
    isbn = cleanstr(isbn)
    print("%s\n"% isbn)

def main():
    for x in books:
        findbook(x)
        findauthor(x)
        findcourse(x)
        findisbn(x)


main()
