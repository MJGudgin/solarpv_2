# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import service
from .models import product
from .models import certificate
from .serializers import serviceSerializer
from .serializers import productSerializer
from .serializers import certificateSerializer

# Create your views here.

def main(request):
	return render(request, 'solarapp/main.html')

def registration(request):
	return render(request, 'solarapp/registration.html')

def login(request):
	return render(request, 'solarapp/login.html')

def dashboard(request):
	return render(request, 'solarapp/dashboard.html')

class serviceView(viewsets.ModelViewSet):
	queryset = service.objects.all()
	serializer_class = serviceSerializer

class productView(viewsets.ModelViewSet):
	queryset = product.objects.all()
	serializer_class = productSerializer

class certificateView(viewsets.ModelViewSet):
	queryset = certificate.objects.all()
	serializer_class = certificateSerializer
