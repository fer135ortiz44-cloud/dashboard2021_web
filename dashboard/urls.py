from django.urls import path
from .views import (
    inicio, 
    reportes_mensuales, 
    dashboard_comparativo, 
    descargar_reporte_excel,
    vista_analitica_avanzada,
    vista_mercado_tiempo_real,
    vista_agente_guia  # <-- Registramos la nueva vista del bot
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('reportes/mensual/', reportes_mensuales, name='reporte_mensual'),
    path('comparativo/', dashboard_comparativo, name='dashboard_comparativo'),
    path('exportar/excel/', descargar_reporte_excel, name='exportar_ventas_excel'),
    path('analitica/', vista_analitica_avanzada, name='analitica_avanzada'),
    path('mercado/', vista_mercado_tiempo_real, name='mercado_tiempo_real'),
    # --- RUTA OFICIAL PARA EL PUNTO 13 ---
    path('agente-guia/', vista_agente_guia, name='agente_guia'),
]