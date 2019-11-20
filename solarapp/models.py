# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class service(models.Model):
	sid = models.IntegerField()
	name = models.CharField(max_length=50)
	description = models.TextField()
	FI = models.BooleanField()
	frequency = models.CharField(max_length=50)
	standard = models.IntegerField()

	def __str__(self):
		return self.name

class product(models.Model):
	model_number = models.IntegerField()
	product_name = models.CharField(max_length=50)
	cell_technology = models.CharField(max_length=50)
	cell_manufacturer = models.CharField(max_length=50)
	number_of_cells = models.IntegerField()
	number_of_cells_in_series = models.IntegerField()
	number_of_series_strings = models.IntegerField()
	number_of_diodes = models.IntegerField()
	product_length = models.IntegerField()
	product_width = models.IntegerField()
	superstate_type = models.CharField(max_length=50)
	superstate_manufacturer = models.CharField(max_length=50)
	substrate_type = models.CharField(max_length=50)
	substrate_manufacturer = models.CharField(max_length=50)
	frame_type = models.CharField(max_length=50)
	frame_adhesive = models.CharField(max_length=50)
	encapsulate_type = models.CharField(max_length=50)
	encapsulate_manufacturer = models.CharField(max_length=50)
	junction_box_type = models.CharField(max_length=50)
	junction_box_manufacturer = models.CharField(max_length=50)

	def __str__(self):
		return self.name

class certificate(models.Model):
	certificate_number = models.IntegerField()
	cid = models.IntegerField()
	userID = models.IntegerField()
	report_number = models.IntegerField()
	issue_date = models.DateField()
	standard_id = models.IntegerField()
	location_id = models.IntegerField()
	model_number = models.IntegerField()
	
	def __str__(self):
		return self.name
