from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Textbook, Posting, Wishlist
from .forms import AuthenticationForm, UserCreate


def index(request):
    # query = request.GET.get('q')
    # if query:
    #     print("test")
    #     # There was a query entered.
    #     # results = Textbook.objects.filter(textbook_name=query)
    # else:
    #     print("test")
    #     # If no query was entered, simply return all objects
    #     # results = SomeModel.objects.all()
    return render_to_response(
		'textchange/index.html',
		locals(),
		context_instance=RequestContext(request)
		)

def profile(request):
	return render_to_response(
		'textchange/profile.html',
		locals(),
		context_instance=RequestContext(request)
		)

def navbar(request):
    logout(request)
    return HttpResponseRedirect('/')

def accountcreation(request):
    form = UserCreate(request.POST or None)
    form2 = AuthenticationForm(request.POST)
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username = username, password = password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response(
                'textchange/index.html',
                locals(),
                context_instance=RequestContext(request)
                )
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
