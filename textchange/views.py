from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

#from .models import Textbook
#from .forms import AuthenticationForm, TextbookForm, CreateForm
"""
def textbook_info(request):
	textbooks = Textbook.objects.all()
	for x in textbooks:
		print(x.textbook_name)
	return render_to_response('results.html', {'textbooks': textbooks,})

def create_user(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			login(new_user)
			return HttpResponseRedirect('accountcreation.html')
	else:
		form = CreateForm()
	
	return render(request, 'accountcreation.html', {'form': form})
	
def display_seller(request):
	if request.method == 'POST':
		form = TextbookForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = TextbookForm()
	return render(request, 'results.html', {'form': form})
"""
def index(request):
	return render_to_response(
		'textchange/index.html',
		locals(),
		context_instance=RequestContext(request)
		)
		
def accountcreation(request):
	signin_form = AuthenticationForm()
	
	return render_to_response(
		'textchange/accountcreation.html',
		locals(),
		context_instance=RequestContext(request)
		)

def wishlisting(request):
	return render_to_response(
		'textchange/wishlisting.html',
		locals(),
		context_instance=RequestContext(request)
		)

def settings(request):
	return render_to_response(
		'textchange/settings.html',
		locals(),
		context_instance=RequestContext(request)
		)
		
def contact(request):
	return render_to_response(
		'textchange/contact.html',
		locals(),
		context_instance=RequestContext(request)
		)
		
def results(request):
	return render_to_response(
		'textchange/results.html',
		locals(),
		context_instance=RequestContext(request)
		)
