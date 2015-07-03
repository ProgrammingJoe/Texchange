from bs4 import BeautifulSoup
from collections import namedtuple

soup = BeautifulSoup(open("bookstore.html"))

books = soup.findAll("div", { "class" : "textbook-item"})

for x in books:
    for y in x.find("b"):
        print("%s\n"% y)
    for z in x.select("[class~=author]"):
        print("%s\n"% z.contents)
