from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .models import Textbook, Posting, Wishlist
from .forms import AuthenticationForm, UserCreate

def index(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			keywords = []
			keywords = form.cleaned_data['keywords']
			keyword_list = keywords.extend(query.split())
			posts = search_for_keywords(keyword_list)
			if posts:
				return render_to_response('textchange/index.html') # Redirect after POST
	"""
	http://zeth.net/archive/2009/11/29/basic-django-search/
	"""
	##############
	"""keywords = []
    while '"' in query:
        first_quote = query.find('"')
        second_quote = query.find('"', first_quote + 1)
        quoted_keywords = query[first_quote:second_quote + 1]
        keywords.append(quoted_keywords.strip('"'))
        query = query.replace(quoted_keywords, ' ')
    # Split the rest by spaces
    keywords.extend(query.split())
    return keywords

MYQUERY = Django form "aggregated values
#split_query_into_keywords(MYQUERY)
	######################
"""

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
