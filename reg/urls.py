
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'reg.views.home'),
    url(r'^login/$', 'reg.views.do_login'),
    url(r'^logout/$', 'reg.views.do_logout'),
)
