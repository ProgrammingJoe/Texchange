from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from functools import reduce
import operator
from django.db.models import Q

from .models import Textbook, Posting, Wishlist
from .forms import AuthenticationForm, UserCreate, Search


def index(request):
    form3 = Search(request.POST or None)
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
		'textchange/index.html',
		locals(),
		context_instance=RequestContext(request)
		)

def textbook(request, uisbn):
    ltextbook = Textbook.objects.filter(isbn = uisbn)
    text = ltextbook[0]
    wishlists = Wishlist.objects.filter(textbook = text)
    listings = Posting.objects.filter(textbook = text)
    return render_to_response(
		'textchange/textbook.html',
		locals(),
		context_instance=RequestContext(request)
		)

def navbar(request):
    logout(request)
    return HttpResponseRedirect('/')

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

def thanks(request):
    return render_to_response(
        'textchange/thanks.html',
        locals(),
        context_instance=RequestContext(request)
        )

def error(request):
    return render_to_response(
        'textchange/error.html',
        locals(),
        context_instance=RequestContext(request)
        )

def results(request):
	return render_to_response(
		'textchange/results.html',
		locals(),
		context_instance=RequestContext(request)
		)

@login_required
def wishlisting(request):
	return render_to_response(
		'textchange/wishlisting.html',
		locals(),
		context_instance=RequestContext(request)
		)

@login_required
def settings(request):
	return render_to_response(
		'textchange/settings.html',
		locals(),
		context_instance=RequestContext(request)
		)

@login_required
def contact(request, uuser, uisbn):
    ltextbook = Textbook.objects.filter(isbn = uisbn)
    text = ltextbook[0]
    return render_to_response(
        'textchange/contact.html',
        locals(),
        context_instance=RequestContext(request)
        )
