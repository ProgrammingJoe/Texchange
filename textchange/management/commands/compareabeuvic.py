from bs4 import BeautifulSoup
from collections import namedtuple

import os
from django.core.management.base import BaseCommand, CommandError
from textchange.models import Textbook



class Command(BaseCommand):

    # Main function to call all the methods
    def handle(self, *args, **options):
        print("test")
