from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from django.db.models import Q
from textchange.models import Textbook

# This command is used to scrape the UVicBookstore of their textbook information
# The html of the bookstore must be put into bookstore.html
# It can be called with 'python manage.py scrapebookstore'


class Command(BaseCommand):

    # Clean up garbage off the string before saving in the db
    def cleanstr(self, str):
        str = str.replace('\n', '')
        str = str.replace(' ', '')
        return str

    # Get the textbook name
    def findbook(self, x):
        title = x.find("span", {"class": "textbook-results-title"})
        if len(title.contents) > 4:
            title = title.contents[4]
        else:
            title = title.contents[2]
        title = title.replace('  ', '')
        title = title.replace('\n', '')
        return title

    # Get the textbook author
    # Find all spans in x with class author
    def findauthor(self, x):
        tag = x.find("span", {"class": "textbook-results-author"})
        author = tag.contents[0]
        author = self.cleanstr(author)
        author = author.replace("Author:", "")
        return author

    # Get the course name
    # Find all divs with class row course-info for the parentx3 of x
    def findcourse(self, x):
        parent = x.parent
        parent = parent.parent
        parent = parent.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling.previous_sibling
        info = parent.find("div", {"class": "six columns"})
        coursetag = info.find('h3')
        course = coursetag.string
        course = course[:8]
        course = self.cleanstr(course)
        return course

    # Get the isbn of the book
    # Get the first div with class row in x
    def findisbn(self, x):
        secondrow = x.findAll("a", {"class": "textbook-results-skew"})[0]
        isbn = secondrow.string
        isbn = self.cleanstr(isbn)
        return isbn

    # Main function to call all the methods
    def handle(self, *args, **options):
        # print(os.listdir("."))
        # Open up the bookstore.html into soup
        soup = BeautifulSoup(open("bookstore.html"), "html.parser")
        books = soup.findAll("div", {"class": "textbook-item"})
        # print(soup.prettify())
        bookmodels = []
        # Loop through all books, find all information and save to the database
        for x in books:
            book = self.findbook(x)
            author = self.findauthor(x)
            course = self.findcourse(x)
            isbn = self.findisbn(x)
            print(book + " ||| " + author + " ||| " + course + " ||| " + isbn)
            object = {
                'book': book,
                'author': author,
                'course': course,
                'isbn': isbn,
            }
            bookmodels.append(object)

        # for dic in bookmodels:
        #     ltextbook = Textbook.objects.filter(Q(isbn=dic['isbn']) & Q(class_name=dic['course']))
        #     if ltextbook:
        #         Textbook.objects.filter(Q(isbn=dic['isbn']) & Q(class_name=dic['course'])).update(semester="FALL2016")
        #     else:
        #         new = Textbook(textbook_name=dic['book'], class_name=dic['course'], author=dic['author'], isbn=dic['isbn'], semester="FALL2016")
        #         new.save()
