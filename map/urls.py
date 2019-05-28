from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index , name='index'),
	url(r'^$', views.map , name='map'),
	url(r'^$', views.boothmap , name='boothmap'),
	url(r'^$', views.inf , name='inf'),
	url(r'^$', views.edit , name='edit'),
	url(r'^$', views.add , name='add'),
	url(r'^$', views.login , name='login'),
	url(r'^$', views.logout , name='logout'),
	url(r'^$', views.register , name='register'),
	url(r'^$', views.search , name='search'),
	url(r'^$', views.lovepage , name='lovepage'),
	url(r'^$', views.comment , name='comment'),
	url(r'^$', views.about , name='about'),
	url(r'^$', views.news , name='news'),
]