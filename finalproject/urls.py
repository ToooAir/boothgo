"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt
from django.views.static import serve
from django.views.generic.base import RedirectView

from map import views
from map.views import *

from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', include('map.urls')),
    url(r'^map/$', map, name='map'),
    url(r'^map/m(?P<id>[0-9]+)/$', boothmap, name='boothmap'),
    url(r'^map/m(?P<id>[0-9]+)/i(?P<pk>[0-9]+)/$', inf, name='inf'),
    url(r'^map/m(?P<id>[0-9]+)/i(?P<pk>[0-9]+)/edit/$',
        csrf_exempt(edit), name='edit'),
    url(r'^map/m(?P<id>[0-9]+)/add/$', csrf_exempt(add), name='add'),
    url(r'^login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^register/', register, name='register'),
    url(r'^search/', search, name='search'),
    url(r'^lovepage/', lovepage, name='lovepage'),
    url(r'^contact/', comment, name='comment'),
    url(r'^about/', about, name='about'),
    url(r'^news/', news, name='news'),
    url(r'^.*$', RedirectView.as_view(url='index/', permanent=False), name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
