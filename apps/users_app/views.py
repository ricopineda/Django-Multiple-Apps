# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
# the index function is called when root is visited
def index(request):
	response = "Hello, I am your USERS request!"
	return HttpResponse(response)

def register(request):
	response = "Hello, I am your REGISTER ROUTE request!"
	return HttpResponse(response)

def login(request):
	response = "Hello, I am your REGISTER LOGIN request!"
	return HttpResponse(response)

def new(request):
	response = "Hello, I am your REGISTER NEW request!"
	return HttpResponse(response)

def display(request):
	response = "Hello, I am your DISPLAY request!"
	return HttpResponse(response)