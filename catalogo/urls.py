from django.urls import path

from . import views

urlpatterns = [

	path('', views.index, name = 'index'),
	path('borrarProducto/<id>', views.borrarProducto, name = 'borrarProducto'),
	path('agregarProducto', views.agregarProducto, name = 'agregarProducto')
] 
