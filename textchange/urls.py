from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

# Urls used to specify what urls are displayed
# with respect to which views function is called
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^login/(?P<route>(\w))$', views.login, name="login"),
    url(r'^wishlisting$', views.wishlisting, name="wishlisting"),
    url(r'^wishlisting/(?P<uisbn>(\w)+)$', views.removewishlisting, name="removewishlisting"),
    url(r'^(?P<urlstring>(query=(\w)+(_(\w)+)*))$', views.results, name="results"),
    url(r'^posting$', views.addposting, name="addposting"),
    url(r'^(?P<urlstring>(query=(\w)+(_(\w)+)*))/(?P<uid>(\w)+)$', views.contactpost, name="contactpost"),
    url(r'^navbar$', views.navbar, name="navbar"),
    url(r'^contact$', views.about, name="about"),
    url(r'^help$', views.help, name="help"),
    url(r'^help/privacypolicy$', views.fbpolicy, name="fbpolicy"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'views.page_not_found'
