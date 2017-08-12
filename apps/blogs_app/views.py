# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "Hello, This is your BLOG request!"
	return HttpResponse(response)

def new(request):
	response = "Hello, This is your NEW route request!"
	return HttpResponse(response)

def show(request, number):

	return HttpResponse("placeholder to display blog" + number)

def edit(request, number):

	return HttpResponse("placeholder to display blog in EDIT route" + " " + number)

def delete(request, number):

	return HttpResponse("placeholder to display blog " + number + " in DELETE route")
