from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^accountcreation$', views.accountcreation, name="accountcreation"),
	url(r'^wishlisting$', views.wishlisting, name="wishlisting"),
	url(r'^wishlisting/(?P<uisbn>(\w)+)$', views.removewishlisting, name="removewishlisting"),
	url(r'^settings$', views.settings, name="settings"),
	url(r'^results$', views.results, name="results"),
	url(r'^results/(?P<uisbn>(\w)+)$', views.textbook, name="textbook"),
	url(r'^results/(?P<uisbn>(\w)+)/(?P<uuser>(\w)+)$', views.contact, name="contact"),
	url(r'^navbar$', views.navbar, name="navbar"),
	url(r'^thanks$', views.thanks, name="thanks"),
	url(r'^error$', views.error, name="error"),
	url(r'^aboutme$', views.about, name="about"),
	url(r'^contactme$', views.contactme, name="contactme"),
]
