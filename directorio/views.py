from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

from directorio.models import Tienda, TiendaForm
from catalogo.models import Inventario, InventarioForm, Producto

# Lista de todas las tiendas
def tiendas(request):
	tiendas = Tienda.objects.order_by('nombre')[:5]
	template = loader.get_template('directorio/tiendas.html')
	context = { 'tiendas':tiendas }
	return HttpResponse(template.render(context, request))

def agregarTienda(request):
	if request.method == 'POST':
		form = TiendaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('tiendas') 
	else:
		form = TiendaForm()
	return render(request, 'directorio/agregarTienda.html', { 'form':form })

def borrarTienda(request, id):
	tienda = Tienda.objects.get(pk = id)
	if(tienda is not None):
		tienda.delete()
	return redirect('tiendas')
