from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^accountcreation$', views.accountcreation, name="accountcreation"),
	url(r'^wishlisting$', views.wishlisting, name="wishlisting"),
	url(r'^settings$', views.settings, name="settings"),
	url(r'^results$', views.results, name="results"),
	url(r'^results/textbook/$', views.textbook, name="textbook"),
	url(r'^results/textbook/contact$', views.contact, name="contact"),
	url(r'^profile$', views.profile, name="profile"),
	url(r'^navbar$', views.navbar, name="navbar"),
	url(r'^thanks$', views.thanks, name="thanks"),
	url(r'^error$', views.error, name="error"),
]
