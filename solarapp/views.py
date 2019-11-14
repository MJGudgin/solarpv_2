# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.

def main(request):
	return render(request, 'solarapp/main.html')

def registration(request):
	return render(request, 'solarapp/registration.html')

def login(request):
	return render(request, 'solarapp/login.html')

def dashboard(request):
	return render(request, 'solarapp/dashboard.html')
