from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^productos', views.ListProductos.as_view(),name="listProductos"),
	url(r'^producto/(?P<slug>[-\w]+)/$', views.DetailProducto.as_view(), name='detailProducto'),
]