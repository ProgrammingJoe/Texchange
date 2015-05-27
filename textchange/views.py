from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Textbook
from .forms import AuthenticationForm, UserCreate

def register(request):
	#if request.method =='POST':
	form = UserCreate(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)#User.objects.create_user(form.cleaned_data['username'], None, form.cleaned_data['password'])
		user.save()
		return render_to_response('textchange/index.html') # Redirect after POST

	return render_to_response('results.html', {
		'form': form,
		},context_instance=RequestContext(request))
	


def index(request):
	return render_to_response(
		'textchange/index.html',
		locals(),
		context_instance=RequestContext(request)
		)
		
def accountcreation(request):
	#signin_form = AuthenticationForm()
	form = UserCreate
	
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
