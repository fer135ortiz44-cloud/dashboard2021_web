from django.urls import path
# 1. Agregamos 'descargar_reporte_excel' a la importación
from .views import inicio, reportes_mensuales, comparativo_vendedores, descargar_reporte_excel

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reportes-mensuales/', reportes_mensuales, name='reportes_mensuales'),
    path('comparativo/', comparativo_vendedores, name='comparativo_vendedores'),
    # 2. Agregamos la ruta física para el botón de Excel
    path('descargar-excel/', descargar_reporte_excel, name='descargar_excel'),
]