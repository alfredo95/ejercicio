from django.urls import path 

from . import views

urlpatterns = [

	path('', views.tiendas, name = 'tiendas'),
	path('agregarTienda', views.agregarTienda, name = 'agregarTienda'),
	path('borrarTienda/<int:id>', views.borrarTienda, name = 'borrarTienda'), 

 

]