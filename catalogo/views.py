from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.decorators import login_required

from catalogo.models import Producto, ProductoForm
from directorio.models import Tienda, TiendaForm
from catalogo.models import Inventario, InventarioForm

# Pagina inicial
def home(request):
	productos = Producto.objects.order_by('nombre')[:5]
	template = loader.get_template('catalogo/home.html')
	context = { 'productos': productos, }
	return HttpResponse(template.render(context, request))


# lista de todos los productos
def index(request):
	template = loader.get_template('catalogo/index.html')
	context = { 'sipi':'sipi' }
	return HttpResponse(template.render(context, request))

# Eliminacion de producto
def borrarProducto(request, id):
	producto = Producto.objects.get(pk=id)
	if(producto is not None):
		producto.delete()
	return redirect('home')

# Formulario / registro de nuevo producto
def agregarProducto(request):
	if request.method == 'POST':
		form = ProductoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form  = ProductoForm()
	return render(request, 'catalogo/agregarProducto.html', {'form':form})

def editarProducto(request, codigo):
	if request.method == 'POST':
		producto = Producto.objects.get(pk=codigo)
		form = ProductoForm(request.POST, instance = producto)
		if form.is_valid():
			form.save()
		
	else:
		producto = Producto.objects.get(pk=codigo)
		if producto is not None:
			form = ProductoForm(instance = producto)
			form.fields['codigo'].widget.attrs['readonly'] = True
			return render(request, 'catalogo/editarProducto.html', {'form':form, 'codigo_producto':codigo})
	return redirect('editarProducto', codigo)


# Lista de todos los productos en el inventario de una tienda
def inventarioTienda(request, id):
	tienda = Tienda.objects.get(id = id)
	if tienda is not None:
		inventarios = Inventario.objects.filter(tienda = tienda).order_by('producto')
		productos = Producto.objects.all()
		template = loader.get_template('directorio/inventarioTienda.html')
		# Form para añadir producto a una tienda
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

# Actualizar cantidad de productos en inventario
def actualizarInventario(request, id):
	if request.method == 'POST':
		inventario = Inventario.objects.get(pk = request.POST.get('inventario'))
		
		if inventario is not None:
			inventario.cantidad = request.POST.get('cantidad')
			inventario.save()
			return redirect('inventarioTienda', id)

	return redirect('index')

