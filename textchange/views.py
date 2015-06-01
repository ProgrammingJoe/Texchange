from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login

from .models import Textbook
from .forms import AuthenticationForm, UserCreate

def index(request):
	return render_to_response(
		'textchange/index.html',
		locals(),
		context_instance=RequestContext(request)
		)

			
def accountcreation(request):


	form = UserCreate(request.POST or None)
	form2 = AuthenticationForm(request.POST or None)
	username = request.POST.get['username']
	password = request.POST.get['password']
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
