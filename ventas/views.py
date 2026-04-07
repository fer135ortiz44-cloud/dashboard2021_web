from django.shortcuts import render
from .models import Venta

def lista_ventas(request):
    ventas = Venta.objects.select_related(
        'cliente', 'sucursal', 'vendedor', 'metodo_pago'
    ).all().order_by('-fecha')
    return render(request, 'ventas/lista_ventas.html', {'ventas': ventas})