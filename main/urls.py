from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Home.as_view(),name="home"),
	url(r'^nosotros/$', views.Nosotros.as_view(),name="nosotros"),
	url(r'^contacto/$', views.Nosotros.as_view(),name="contacto"),
]