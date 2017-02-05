from django.shortcuts import render_to_response, RequestContext
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.db.models import Q
from smtplib import SMTPException

from .models import Textbook, Posting, User, Feedback
from .forms import Search, PostCreate, Contact


# Index page of the site
# Consists of search form
# input is split into keywords and queuried on all textbook attributes
# The number of results is also calculated for the user
def index(request):
    homepage = "homepage"
    curuser = request.user
    form3 = Search(request.POST or None)
    query = request.POST.get('search')
    school = request.POST.get('school')

    if form3.is_valid() and request.POST:
        keywords = []
        if query and school:
            keywords = query.split()
            urlstring = "query="
            for word in keywords:
                if word == keywords[0]:
                    urlstring += word
                else:
                    urlstring += "_" + word
            return HttpResponseRedirect("/%s" % urlstring)
        else:
            print("You're supposed to type something idiot\n")
    else:
        return render_to_response(
            'textchange/index.html',
            locals(),
            context_instance=RequestContext(request)
            )

    return render_to_response(
        'textchange/index.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Logout functionality in the navbar
def navbar(request):
    logout(request)
    return HttpResponseRedirect('/')


# Renders the about page
def about(request):
    # Handles feedback form and checks if the user has sent too much feedback
    # If the user has already sent more than 3 feedbacks, don't save feedback
    if request.method == 'GET':
        form = Contact()
    else:
        form = Contact(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            email = form.cleaned_data['email']
            try:
                new = Feedback(email=email, content=content, subject=subject, name=name)
                new.save()
                message = "Message Sent Successfully"
                return render_to_response(
                    'textchange/about.html',
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

    query = Posting.objects.filter(textbook__in=query)
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
    postings = Posting.objects.filter(user=curuser)

    return render_to_response(
        'textchange/wishlisting.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Renders the add a posting form page
@login_required
def addposting(request):
    form = PostCreate(request.POST or None, request.FILES or None)

    # Get textbook with isbn equal to usibn
    curuser = request.user

    isbn = request.POST.get('ISBN')
    school = request.POST.get('school')

    if(isbn and school):
        file_s = Textbook.objects.filter(shortschool=school).values_list('isbn', flat=True)
        if(isbn in file_s and form.is_valid() and request.POST):
            condition = request.POST.get('condition')
            price = request.POST.get('price')
            image = request.FILES.get('image')
            comments = request.POST.get('comments')
            isbn = request.POST.get('ISBN')
            text = Textbook.objects.get(isbn=isbn)
            querystring = "query=" + isbn
            print(querystring)
            print(text)
            if image:
                if (not (Posting.objects.filter(user=curuser, textbook=text))):
                    new = Posting(textbook=text, user=curuser, post_date=datetime.now(), condition=condition, price=price, image=image, comments=comments)
                    new.save()
                    return HttpResponseRedirect('/' + querystring + '/' + str(new.id))
            else:
                if (not (Posting.objects.filter(user=curuser, textbook=text))):
                    new = Posting(textbook=text, user=curuser, post_date=datetime.now(), condition=condition, price=price, comments=comments)
                    new.save()
                    return HttpResponseRedirect('/' + querystring + '/' + str(new.id))
        else:
            if(isbn not in file_s and len(str(isbn)) == 13):
                notexisting = True

            return render_to_response(
                'textchange/addposting.html',
                locals(),
                context_instance=RequestContext(request)
                )
            # 9780131873254
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
        if request.POST.get("DeletePosting"):
            Posting.objects.filter(user=curuser, textbook=text).delete()

    return HttpResponseRedirect('/wishlisting')


# Renders the page used to view textbook and contact info
# for a specific book and user
@login_required
def contactpost(request, uid, urlstring):
    # Get the textbook and user for the posting selected
    posting = Posting.objects.get(id=uid)
    quser = User.objects.get(id=posting.user_id)
    curuser = request.user

    if(quser == curuser):
        bookowner = True

    if quser.social_auth.filter(provider='facebook'):
        social = quser.social_auth.get(provider='facebook')
    elif quser.social_auth.filter(provider='google-oauth2'):
        social = quser.social_auth.get(provider='google-oauth2')

    return render_to_response(
        'textchange/contactpost.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Render login page
def login(request):
    return render_to_response(
        'textchange/login.html',
        locals(),
        context_instance=RequestContext(request)
        )


# Render facebook policy page
def fbpolicy(request):
    return render_to_response(
        'textchange/fbpolicy.html',
        locals(),
        context_instance=RequestContext(request)
        )


# HTTP Error 404
# def page_not_found(request):
#     response = render_to_response(
#         '404.html',
#         context_instance=RequestContext(request)
#     )
#     response.status_code = 404
#     return response

#
# # HTTP Error 500
# def server_error(request, exception, template_name='500.html'):
#     response = render_to_response(
#         '500.html',
#         context_instance=RequestContext(request)
#     )
#     response.status_code = 500
#     return response
