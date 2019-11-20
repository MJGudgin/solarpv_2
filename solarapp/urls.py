from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView

from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.productView)
router.register('certificate', views.certificateView)
router.register('service', views.serviceView)

urlpatterns = [
	url(r'^main$', views.main),
	url(r'^registration$', views.registration),
	url(r'^login$', views.login),
	url(r'^dashboard$', views.dashboard),
	url('', include(router.urls))

]


