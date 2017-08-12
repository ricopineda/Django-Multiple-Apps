from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^register/$', views.register),
	url(r'^login/$', views.login),
	url(r'^users/new/$', views.new),
	url(r'^users-display/$', views.display)

]