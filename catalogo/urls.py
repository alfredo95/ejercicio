from django.urls import path

from . import views

urlpatterns = [

	path('', views.index, name = 'index'),
	path('producto', views.home, name = 'home'),
	path('editarProducto/<codigo>', views.editarProducto, name = 'editarProducto'),
	path('borrarProducto/<id>', views.borrarProducto, name = 'borrarProducto'),
	path('agregarProducto', views.agregarProducto, name = 'agregarProducto'),
	path('inventarioTienda/<int:id>', views.inventarioTienda, name = 'inventarioTienda'),
	path('borrarInventario/<int:id>', views.borrarInventario, name = 'borrarInventario'),
	path('agregarInventario/<int:id>', views.agregarInventario, name = 'agregarInventario'), 
	path('actualizarInventario/<int:id>', views.actualizarInventario, name = 'actualizarInventario'), 
] 
