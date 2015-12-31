from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

# Urls used to specify what urls are displayed
# with respect to which views function is called
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^wishlisting$', views.wishlisting, name="wishlisting"),
    url(r'^wishlisting/(?P<uisbn>(\w)+)$', views.removewishlisting, name="removewishlisting"),
    url(r'^results$', views.results, name="results"),
    url(r'^results/(?P<uisbn>(\w)+)$', views.textbook, name="textbook"),
    url(r'^results/(?P<uisbn>(\w)+)/posting/add$', views.addposting, name="addposting"),
    url(r'^results/(?P<uisbn>(\w)+)/(?P<uuser>(\w)+)/post$', views.contactpost, name="contactpost"),
    url(r'^results/(?P<uisbn>(\w)+)/(?P<uuser>(\w)+)/wish$', views.contactwish, name="contactwish"),
    url(r'^navbar$', views.navbar, name="navbar"),
    url(r'^thanks$', views.thanks, name="thanks"),
    url(r'^contact$', views.about, name="about"),
    url(r'^help$', views.help, name="help"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
