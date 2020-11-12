from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from catalogo.models import Producto, ProductoForm

from directorio.models import Tienda, TiendaForm
from catalogo.models import Inventario, InventarioForm

# Pagina inicial / lista de todos los productos
def index(request):
	productos = Producto.objects.order_by('nombre')[:5]
	template = loader.get_template('catalogo/index.html')
	context = { 'productos': productos, }
	return HttpResponse(template.render(context, request))

# Eliminacion de producto
def borrarProducto(request, id):
	producto = Producto.objects.get(pk=id)
	if(producto is not None):
		producto.delete()
	return redirect('index')

# Formulario / registro de nuevo producto
def agregarProducto(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form  = ProductoForm()
	return render(request, 'catalogo/agregarProducto.html', {'form':form})



# Lista de todos los productos en el inventario de una tienda
def inventarioTienda(request, id):
	tienda = Tienda.objects.get(id = id)
	if tienda is not None:
		inventarios = Inventario.objects.filter(tienda = tienda)
		productos = Producto.objects.all()
		template = loader.get_template('directorio/inventarioTienda.html')
		form = InventarioForm()
		form.fields['producto'].empty_label = 'Selecciona un producto'
		form.tienda_id = tienda.id
		context = { 'tienda':tienda, 'inventarios':inventarios, 'productos':productos, 'form': form }
		return HttpResponse(template.render(context, request))	

	return redirect('tiendas')	


# Eliminacion de producto en el inventario de una tienda
def borrarInventario(request, id):
	inventario = Inventario.objects.get(pk=id)
	if inventario is not None:
		tienda = inventario.tienda.id
		inventario.delete()
	return redirect('inventarioTienda', id = tienda)


# Agregar inventario de producto en tienda
def agregarInventario(request, id):
	if request.method == 'POST':
		form = InventarioForm(request.POST)
		if form.is_valid():
			form.save()
	return redirect('inventarioTienda', id = id)

