from django.shortcuts import render_to_response, RequestContext
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from smtplib import SMTPException

from .models import Textbook, Posting, Wishlist, User, Feedback
from .forms import Search, PostCreate, Contact


# Index page of the site
# Consists of search form
# input is split into keywords and queuried on all textbook attributes
# The number of results is also calculated for the user
def index(request):
    curuser = request.user
    form3 = Search(request.POST or None)
    if request.method == 'POST' and form3:
        if request.POST.get("Search"):
            query = request.POST.get('search')
            keywords = []
            if query:
                keywords = query.split()
                urlstring = "query="
                for word in keywords:
                    if word == keywords[0]:
                        urlstring += word
                    else:
                        urlstring += "_" + word
                return HttpResponseRedirect("/%s" % urlstring)
                # return render_to_response(
                #     'textchange/results.html',
                #     locals(),
                #     context_instance=RequestContext(request)
                #     )
            else:
                print("You're supposed to type something idiot\n")

            # if query:
            #     results = []
            #     # Split up the input
            #     # query each attribute of the textbook per word
            #     keywords = query.split()
            #     query = Textbook.objects.all()
            #     for x in keywords:
            #         query = query.filter(Q(class_name__icontains=x) | Q(textbook_name__icontains=x) | Q(author__icontains=x) | Q(isbn__icontains=x))
            #
            #     numresults = len(query)
            #     return render_to_response(
            #         'textchange/results.html',
            #         locals(),
            #         context_instance=RequestContext(request)
            #         )
            # else:
            #     print("You're supposed to type something idiot\n")

    return render_to_response(
        'textchange/index.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Textbook details page
# Consists of add/remove buttons for postings/wishlist
# Buttons change based on state of that textbook and user combination
@login_required
def textbook(request, uisbn, urlstring):
    # Get textbook with isbn equal to usibn
    ltextbook = Textbook.objects.filter(isbn=uisbn)
    text = ltextbook[0]
    numtexts = len(ltextbook)

    # Create lists of postings and wishes for those textbooks
    wishlists = Wishlist.objects.filter(textbook=text)
    listings = Posting.objects.filter(textbook=text)

    # Sort the lists by price and wish_Date
    listings = list(listings)
    wishlists = list(wishlists)
    listings.sort(key=lambda x: x.price)
    wishlists.sort(key=lambda x: x.wish_date)
    curuser = request.user

    # Check to see if there is a posting/wish with the current textbook user combination
    postexist = Posting.objects.filter(user=curuser, textbook=text)
    wishexist = Wishlist.objects.filter(user=curuser, textbook=text)

    # Depending on status of user textbook combination
    # Add or remove postings/wishes
    if request.method == 'POST':
        if request.POST.get("AddWishlist"):
            if (not (Wishlist.objects.filter(user=curuser, textbook=text))):
                new = Wishlist(textbook=text, user=curuser, wish_date=datetime.now())
                new.save()
                return HttpResponseRedirect('/' + urlstring + '/' + uisbn)
        if request.POST.get("DeleteWishlist"):
            Wishlist.objects.filter(user=curuser, textbook=text).delete()
            return HttpResponseRedirect('/' + urlstring + '/' + uisbn)
        if request.POST.get("DeleteListing"):
            Posting.objects.filter(user=curuser, textbook=text).delete()
            return HttpResponseRedirect('/' + urlstring + '/' + uisbn)

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
@login_required
def about(request):
    curuser = request.user

    # Calculates the number of feedbacks this user has given
    numfeedbacks = Feedback.objects.filter(user=curuser)
    numfeedbacks = len(list(numfeedbacks))

    # Handles feedback form and checks if the user has sent too much feedback
    # If the user has already sent more than 3 feedbacks, don't save feedback
    if request.method == 'GET':
        form = Contact()
    else:
        form = Contact(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            email = form.cleaned_data['email']
            if(numfeedbacks >= 4):
                badmessage = "You're on Feedback Timeout now."
                return render_to_response(
                    'textchange/about.html',
                    locals(),
                    context_instance=RequestContext(request)
                    )
            try:
                new = Feedback(email=email, content=content, subject=subject, user=curuser)
                new.save()
                message = "Message Sent Successfully"
                return render_to_response(
                    'textchange/thanks.html',
                    locals(),
                    context_instance=RequestContext(request)
                    )
            except SMTPException:
                print "Error: unable to add feedback"
                message = "Message Failed to Send"
                return render_to_response(
                    'textchange/about.html',
                    locals(),
                    context_instance=RequestContext(request)
                    )

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


# Renders the thank you for creating an account page
@login_required
def thanks(request):
    return render_to_response(
        'textchange/thanks.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Renders the results of a textbook search
def results(request, urlstring):
    curuser = request.user

    form4 = Search(request.POST or None)
    if request.method == 'POST' and form4:
        if request.POST.get("Search"):
            query = request.POST.get('search')
            keywords = []
            if query:
                keywords = query.split()
                urlstring = "query="
                for word in keywords:
                    if word == keywords[0]:
                        urlstring += word
                    else:
                        urlstring += "_" + word
                return HttpResponseRedirect("/%s" % urlstring)
                # return render_to_response(
                #     'textchange/results.html',
                #     locals(),
                #     context_instance=RequestContext(request)
                #     )
            else:
                print("You're supposed to type something idiot\n")


    urlstring = urlstring[6:]
    results = []
    # Split up the input
    # query each attribute of the textbook per word
    keywords = urlstring.split("_")
    query = Textbook.objects.all()
    for x in keywords:
        query = query.filter(Q(class_name__icontains=x) | Q(textbook_name__icontains=x) | Q(author__icontains=x) | Q(isbn__icontains=x))

    urlstring = "query=" + urlstring
    numresults = len(query)
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
    wishlists = Wishlist.objects.filter(user=curuser)
    listings = Posting.objects.filter(user=curuser)

    return render_to_response(
        'textchange/wishlisting.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Renders the add a posting form page
@login_required
def addposting(request, uisbn, urlstring):
    form = PostCreate(request.POST or None, request.FILES or None)

    # Get textbook with isbn equal to usibn
    ltextbook = Textbook.objects.filter(isbn=uisbn)
    text = ltextbook[0]
    curuser = request.user

    # Handles the add posting form
    if form.is_valid() and request.POST:
        condition = request.POST.get('condition')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        comments = request.POST.get('comments')
        if image:
            if (not (Posting.objects.filter(user=curuser, textbook=text))):
                new = Posting(textbook=text, user=curuser, post_date=datetime.now(), condition=condition, price=price, image=image, comments=comments)
                new.save()
                return HttpResponseRedirect('/' + urlstring + '/' + uisbn)
        else:
            if (not (Posting.objects.filter(user=curuser, textbook=text))):
                new = Posting(textbook=text, user=curuser, post_date=datetime.now(), condition=condition, price=price, comments=comments)
                new.save()
                return HttpResponseRedirect('/' + urlstring + '/' + uisbn)

    return render_to_response(
        'textchange/addposting.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Used to delete wishes or postings from the wishlisting page
@login_required
def removewishlisting(request, uisbn):
    # Get the textbook and user
    curuser = request.user
    ltextbook = Textbook.objects.filter(isbn=uisbn)
    text = ltextbook[0]

    # If delete is called query and delete
    if request.method == 'POST':
        if request.POST.get("DeleteWishlist"):
            Wishlist.objects.filter(user=curuser, textbook=text).delete()
        if request.POST.get("DeletePosting"):
            Posting.objects.filter(user=curuser, textbook=text).delete()

    return HttpResponseRedirect('/wishlisting')


# Renders the page used to view textbook and contact info
# for a specific book and user
@login_required
def contactpost(request, uuser, uisbn, urlstring):
    # Get the textbook and user for the posting selected
    ltextbook = Textbook.objects.filter(isbn=uisbn)
    text = ltextbook[0]
    luser = User.objects.filter(pk=uuser)
    quser = luser[0]

    social = quser.social_auth.get(provider='facebook')

    # Query for the posting of the user textbook combination.
    post = Posting.objects.filter(user=quser, textbook=ltextbook)
    posting = post[0]
    return render_to_response(
        'textchange/contactpost.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Renders the page used to view textbook and contact info
# for a specific book and user
@login_required
def contactwish(request, uuser, uisbn, urlstring):
    # Get the textbook and user for the wish selected
    ltextbook = Textbook.objects.filter(isbn=uisbn)
    text = ltextbook[0]
    luser = User.objects.filter(pk=uuser)
    quser = luser[0]

    social = quser.social_auth.get(provider='facebook')

    # Query for the wish of the user textbook combination
    wish = Wishlist.objects.filter(user=quser, textbook=ltextbook)
    wishlist = wish[0]
    return render_to_response(
        'textchange/contactwish.html',
        locals(),
        context_instance=RequestContext(request)
        )


def fbprivacy(request):
    return render_to_response(
        'textchange/privacypolicy.html',
        locals(),
        context_instance=RequestContext(request)
        )


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
