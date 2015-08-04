from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Textbook, Posting, Wishlist
from .forms import AuthenticationForm, UserCreate, Search


def index(request):
    form = Search(request.POST or None)
    query = request.POST.get('search')
    keywords = []
    if query:
        results = []
        keywords = query.split()
        for x in keywords:
            if(Textbook.objects.filter(class_name__icontains=x)):
                res = Textbook.objects.filter(class_name__icontains=x)
                for a in res:
                    results.append(a)
            if(Textbook.objects.filter(textbook_name__icontains=x)):
                res = Textbook.objects.filter(textbook_name__icontains=x)
                for a in res:
                    results.append(a)
            if(Textbook.objects.filter(author__icontains=x)):
                res = Textbook.objects.filter(author__icontains=x)
                for a in res:
                    results.append(a)
            if(Textbook.objects.filter(isbn__icontains=x)):
                res = Textbook.objects.filter(isbn__icontains=x)
                for a in res:
                    results.append(a)
        print(results)
        return render_to_response(
            'textchange/results.html',
            locals(),
            context_instance=RequestContext(request)
            )
    else:
        print("You're supposed to type something idiot \n")
    # contains
    # Case-sensitive containment test. For example:
    #
    # Entry.objects.get(headline__contains='Lennon')
    # Roughly translates to this SQL:
    #
    # SELECT ... WHERE headline LIKE '%Lennon%';
    # Note this will match the headline 'Today Lennon honored' but not 'today lennon honored'.
    #
    # There’s also a case-insensitive version, icontains.


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

def textbook(request):

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
