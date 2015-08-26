from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from functools import reduce
import operator
from datetime import datetime
from django.db.models import Q

from .models import Textbook, Posting, Wishlist, User
from .forms import AuthenticationForm, UserCreate, Search

# Index page of the site
# Consists of search form in which the input is split into keywords which are then queuried on all textbook attributes
def home(request):
    form3 = Search(request.POST or None)
    if request.method == 'POST':
        if request.POST.get("Search"):
            query = request.POST.get('search')
            keywords = []
            if query:
                results = []
                keywords = query.split()
                for x in keywords:
                    res = Textbook.objects.filter(Q(class_name__icontains = x) | Q(textbook_name__icontains = x) | Q(author__icontains = x) | Q(isbn__icontains = x))
                    for a in res:
                        results.append(a)
                results = list(set(results))
                return render_to_response(
                    'textchange/results.html',
                    locals(),
                    context_instance=RequestContext(request)
                    )
            else:
                print("You're supposed to type something idiot\n")

    return render_to_response(
		'textchange/home.html',
		locals(),
		context_instance=RequestContext(request)
		)

# Textbook details page
# Consists of add/remove buttons for postings/wishlist
# Buttons change based on state of that textbook and user combination
def textbook(request, uisbn):
    # Get textbook with isbn equal to usibn
    ltextbook = Textbook.objects.filter(isbn = uisbn)
    text = ltextbook[0]

    # Create lists of postings and wishes for those textbooks
    wishlists = Wishlist.objects.filter(textbook = text)
    listings = Posting.objects.filter(textbook = text)
    curuser = request.user

    # Check to see if there is a posting/wish with the current textbook user combination
    postexist = Posting.objects.filter(Q(user = curuser) & Q(textbook = text))
    wishexist = Wishlist.objects.filter(Q(user = curuser) & Q(textbook = text))

    # Depending on status of user textbook combination add or remove postings/wishes
    if request.method == 'POST':
        if request.POST.get("AddWishlist"):
            if (not (Wishlist.objects.filter(Q(user = curuser) & Q(textbook = text)))):
                new = Wishlist(textbook = text, user = curuser, wish_date = datetime.now())
                new.save()
        if request.POST.get("AddListing"):
            if (not (Posting.objects.filter(Q(user = curuser) & Q(textbook = text)))):
                new = Posting(textbook = text, user = curuser, post_date = datetime.now(), condition="good", price=".50")
                new.save()
        if request.POST.get("DeleteWishlist"):
            Wishlist.objects.filter(Q(user = curuser) & Q(textbook = text)).delete()
        if request.POST.get("DeleteListing"):
            Posting.objects.filter(Q(user = curuser) & Q(textbook = text)).delete()

    return render_to_response(
		'textchange/textbook.html',
		locals(),
		context_instance=RequestContext(request)
		)

# Logout functionality in the navbar
def navbar(request):
    logout(request)
    return HttpResponseRedirect('/')

# Renders the about page
def about(request):
    return render_to_response(
		'textchange/about.html',
		locals(),
		context_instance=RequestContext(request)
		)

# Renders the help/tutorial page
def help(request):
    return render_to_response(
		'textchange/help.html',
		locals(),
		context_instance=RequestContext(request)
		)

# Temporary index page
def index(request):
    return render_to_response(
		'textchange/index.html',
		locals(),
		context_instance=RequestContext(request)
		)

# Account creation and login page.
# If the user is real, log them in.
# If the user creation form is valid, save the user
def accountcreation(request):
    form = UserCreate(request.POST or None)
    form2 = AuthenticationForm(request.POST or None)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return render_to_response(
                'textchange/error.html',
                locals(),
                context_instance=RequestContext(request)
                )
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return render(request, 'textchange/thanks.html')

    return render_to_response(
        'textchange/accountcreation.html',
        locals(),
        context_instance=RequestContext(request)
        )

# Renders the thank you for creating an account page
def thanks(request):
    return render_to_response(
        'textchange/thanks.html',
        locals(),
        context_instance=RequestContext(request)
        )

# Renders the 404/error page
def error(request):
    return render_to_response(
        'textchange/error.html',
        locals(),
        context_instance=RequestContext(request)
        )

# Renders the results of a textbook search
def results(request):
	return render_to_response(
		'textchange/results.html',
		locals(),
		context_instance=RequestContext(request)
		)

# Renders a page for the user to manage their postings and wishes
@login_required
def wishlisting(request):
    # Creates lists of postings and wishes for that user
    curuser = request.user
    wishlists = Wishlist.objects.filter(user = curuser)
    listings = Posting.objects.filter(user = curuser)

    return render_to_response(
	   'textchange/wishlisting.html',
       locals(),
       context_instance=RequestContext(request)
       )

# Used to delete wishes or postings from the wishlisting page
@login_required
def removewishlisting(request, uisbn):
    # Get the textbook and user
    curuser = request.user
    ltextbook = Textbook.objects.filter(isbn = uisbn)
    text = ltextbook[0]

    # If delete is called query and delete
    if request.method == 'POST':
        if request.POST.get("DeleteWishlist"):
            Wishlist.objects.filter(Q(user = curuser) & Q(textbook = text)).delete()
        if request.POST.get("DeletePosting"):
            Posting.objects.filter(Q(user = curuser) & Q(textbook = text)).delete()

    return HttpResponseRedirect('/wishlisting')

# Renders the page used to view textbook and contact info for a specific book and user
@login_required
def contactpost(request, uuser, uisbn):
    # Get the textbook and user for the posting selected
    ltextbook = Textbook.objects.filter(isbn = uisbn)
    text = ltextbook[0]
    luser = User.objects.filter(username = uuser)
    quser = luser[0]

    # Query for the posting of the user textbook combination.
    post = Posting.objects.filter((Q(user = quser) & Q(textbook = ltextbook)))
    posting = post[0]
    return render_to_response(
        'textchange/contactpost.html',
        locals(),
        context_instance=RequestContext(request)
        )
# Renders the page used to view textbook and contact info for a specific book and user
@login_required
def contactwish(request, uuser, uisbn):
    # Get the textbook and user for the wish selected
    ltextbook = Textbook.objects.filter(isbn = uisbn)
    text = ltextbook[0]
    luser = User.objects.filter(username = uuser)
    quser = luser[0]

    # Query for the wish of the user textbook combination
    wish = Wishlist.objects.filter((Q(user = quser) & Q(textbook = ltextbook)))
    wishlist = wish[0]
    return render_to_response(
        'textchange/contactwish.html',
        locals(),
        context_instance=RequestContext(request)
        )
