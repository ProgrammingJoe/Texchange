from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Textbook, Posting, Wishlist
from .forms import AuthenticationForm, UserCreate

def search(request):
    query = request.GET.get('q')
    if query:
        # There was a query entered.
        results = SomeModel.objects.filter(somefield=query)
    else:
        # If no query was entered, simply return all objects
        results = SomeModel.objects.all()
    return render_to_response(
		'textchange/results.html',
		locals(),
		context_instance=RequestContext(request)
		)

def index(request):

	return render_to_response(
		'textchange/index.html',
		locals(),
		context_instance=RequestContext(request)
		)


def accountcreation(request):
	form = UserCreate(request.POST)
	form2 = AuthenticationForm(request.POST)
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username = username, password = password)

	if form.is_valid():
		user = form.save(commit=False)
		user.save()
		return render_to_response('textchange/index.html') # Redirect after POST
	if user is not None:
		if user.is_active:
			login(request, user)
			return render_to_response('textchange/index.html') # Redirect after success
		else:
			return render_to_response('textchange/accountcreation.html')


	return render_to_response(
		'textchange/accountcreation.html',
		locals(),
		context_instance=RequestContext(request)
		)

def results(request):
	posting_info = Posting.objects.all()
	wishlist_info = Wishlist.objects.all()
	textbook_info = Textbook.objects.all()

	textbook_items = {
		"textbook_info" : textbook_info
	}
	posting_items = {
		"posting_info" : posting_info
	}
	wishlist_items = {
		"wishlist_info" : wishlist_info
	}

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
def contact(request):
	return render_to_response(
		'textchange/contact.html',
		locals(),
		context_instance=RequestContext(request)
		)
