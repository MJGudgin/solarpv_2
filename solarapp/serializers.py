from rest_framework import serializers
from .models import service
from .models import product
from .models import certificate

class serviceSerializer(serializers.ModelSerializer):
	class Meta:
		model = service
		fields = ('id', 'sid', 'name', 'description', 'FI', 'frequency', 'standard')

class productSerializer(serializers.ModelSerializer):
	class Meta:
		model = product
		fields = ('model_number', 
			'product_name', 
			'cell_technology', 
			'cell_manufacturer', 
			'number_of_cells',
			'number_of_cells_in_series',
			'number_of_series_strings',
			'number_of_diodes',
			'product_length',
			'product_width',
			'superstate_type',
			'superstate_manufacturer',
			'substrate_type',
			'substrate_manufacturer',
			'frame_type',
			'frame_adhesive',
			'encapsulate_type',
			'encapsulate_manufacturer',
			'junction_box_type',
			'junction_box_manufacturer')

class certificateSerializer(serializers.ModelSerializer):
	class Meta:
		model = certificate
		fields = ('certificate_number',
			'cid',
			'userID',
			'report_number',
			'issue_date',
			'standard_id',
			'location_id',
			'model_number')
