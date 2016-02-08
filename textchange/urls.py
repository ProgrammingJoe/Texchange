from django.conf.urls import url
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from django.conf import settings
from django.conf.urls.static import static

from . import views

handler400 = 'views.bad_request'
handler403 = 'views.permission_denied'
handler404 = 'views.page_not_found'
handler500 = 'views.server_error'

# Urls used to specify what urls are displayed
# with respect to which views function is called
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^wishlisting$', views.wishlisting, name="wishlisting"),
    url(r'^wishlisting/(?P<uisbn>(\w)+)$', views.removewishlisting, name="removewishlisting"),
    url(r'^(?P<urlstring>(query=(\w)+(_(\w)+)*))$', views.results, name="results"),
    url(r'^(?P<urlstring>(query=(\w)+(_(\w)+)*))/(?P<uisbn>(\w)+)$', views.textbook, name="textbook"),
    url(r'^(?P<urlstring>(query=(\w)+(_(\w)+)*))/(?P<uisbn>(\w)+)/posting/add$', views.addposting, name="addposting"),
    url(r'^(?P<urlstring>(query=(\w)+(_(\w)+)*))/(?P<uisbn>(\w)+)/(?P<uuser>(\w)+)/post$', views.contactpost, name="contactpost"),
    url(r'^(?P<urlstring>(query=(\w)+(_(\w)+)*))/(?P<uisbn>(\w)+)/(?P<uuser>(\w)+)/wish$', views.contactwish, name="contactwish"),
    url(r'^navbar$', views.navbar, name="navbar"),
    url(r'^thanks$', views.thanks, name="thanks"),
    url(r'^contact$', views.about, name="about"),
    url(r'^help$', views.help, name="help"),
    url(r'^help/privacypolicy$', views.fbpolicy, name="fbpolicy"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
