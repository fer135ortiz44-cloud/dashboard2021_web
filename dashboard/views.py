from django.shortcuts import render
from django.db.models import Sum, Count, Max
from django.db.models.functions import ExtractMonth  # <-- Esto es la clave
import json
from ventas.models import Venta
from catalogos.models import Cliente, Vendedor

def inicio(request):
    ventas = Venta.objects.all()
    
    # Cálculos Matemáticos
    total_ventas = ventas.aggregate(total=Sum('total'))['total'] or 0
    total_documentos = ventas.count()
    ticket_promedio = total_ventas / total_documentos if total_documentos > 0 else 0
    venta_maxima = ventas.aggregate(maximo=Max('total'))['maximo'] or 0

    # Datos para las Gráficas
    por_metodo = list(ventas.values('metodo_pago__nombre').annotate(total=Sum('total')))
    por_vendedor = list(ventas.values('vendedor__nombre').annotate(total=Sum('total')))

    contexto = {
        'total_ventas': round(total_ventas, 2),
        'total_documentos': total_documentos,
        'ticket_promedio': round(ticket_promedio, 2),
        'venta_maxima': round(venta_maxima, 2),
        'ventas_por_metodo_json': json.dumps(por_metodo, default=str),
        'ventas_por_vendedor_json': json.dumps(por_vendedor, default=str),
    }
    return render(request, 'dashboard/inicio.html', contexto)

def reportes_mensuales(request):
    # Usamos ExtractMonth para crear un campo llamado 'mes' que sea fácil de leer
    ventas_mes = list(Venta.objects.annotate(mes=ExtractMonth('fecha'))
                     .values('mes')
                     .annotate(total=Sum('total'))
                     .order_by('mes'))
    
    contexto = {
        'ventas_mes_json': json.dumps(ventas_mes, default=str),
    }
    return render(request, 'dashboard/reportes_mensuales.html', contexto)

def comparativo_vendedores(request):
    comparativo = list(Vendedor.objects.annotate(num_ventas=Count('venta')).values('nombre', 'num_ventas'))
    contexto = {
        'comparativo_json': json.dumps(comparativo, default=str),
    }
    return render(request, 'dashboard/comparativo.html', contexto)

# --- AGREGA ESTOS IMPORTS HASTA ARRIBA DEL ARCHIVO ---
from django.http import HttpResponse
import pandas as pd
# ----------------------------------------------------

# --- PEGA ESTA FUNCIÓN AL FINAL DEL ARCHIVO ---
def descargar_reporte_excel(request):
    # Traemos los datos de las ventas para el reporte
    ventas = Venta.objects.all().values(
        'folio', 'fecha', 'cliente__nombre', 'sucursal__nombre', 'vendedor__nombre', 'total'
    )
    
    # Creamos el archivo Excel usando pandas (Proceso ETL: Transform/Load)
    df = pd.DataFrame(list(ventas))
    df.columns = ['Folio', 'Fecha', 'Cliente', 'Sucursal', 'Vendedor', 'Total']

    # Configuramos la respuesta para que el navegador lo descargue
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Reporte_Ventas_2021.xlsx"'
    
    # Guardamos el contenido en el archivo de respuesta
    df.to_excel(response, index=False)
    return response