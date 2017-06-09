from django.conf.urls import url
from django.contrib import admin
from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	 url(r'^$', post_list , name='list'),
 	 url(r'^create/$', post_create), #2nd part here post_create is the name of the view
 	 url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'), #this name can be used directly in a href in html files ealier we have to put whole url
 	 url(r'^(?P<slug>[\w-]+)/edit/$', post_update ,name='update'),
 	 url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
 	 url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),



 	 ]