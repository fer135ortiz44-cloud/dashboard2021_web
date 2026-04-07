import pandas as pd
import random
from datetime import datetime, timedelta

# Nombres ficticios para tu tienda
categorias = ["Bebidas", "Botanas", "Lácteos", "Abarrotes", "Limpieza"]
sucursales = ["Norte", "Sur", "Centro", "Oriente"]
ciudades = ["Ciudad de México", "Guadalajara", "Monterrey", "Puebla"]
estados = ["CDMX", "Jalisco", "Nuevo León", "Puebla"]
metodos_pago = ["Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito", "Transferencia"]
clientes = ["Juan Pérez", "María García", "Luis Hernández", "Ana Martínez", "Pedro Gómez"]
vendedores = ["Carlos Slim", "Roberto Gómez", "Laura Pausini", "Diego Luna"]
productos = [
    ("B01", "Coca Cola 600ml", "Bebidas", 20.00), ("B02", "Jugo Jumex 1L", "Bebidas", 35.00),
    ("S01", "Papas Sabritas", "Botanas", 22.00), ("S02", "Doritos Nacho", "Botanas", 24.00),
    ("L01", "Leche Lala 1L", "Lácteos", 28.00), ("L02", "Queso Panela", "Lácteos", 45.00),
    ("A01", "Frijoles Isadora", "Abarrotes", 20.00), ("A02", "Arroz Verde Valle", "Abarrotes", 32.00),
    ("C01", "Cloralex 1L", "Limpieza", 25.00), ("C02", "Fabuloso", "Limpieza", 30.00)
]

# Configuración
num_ventas = 200 # Generaremos 200 ventas
fecha_inicio = datetime(2021, 1, 1)

datos = []
folio_actual = 1

for i in range(num_ventas):
    folio = f"V-{str(folio_actual).zfill(4)}"
    fecha = fecha_inicio + timedelta(days=random.randint(0, 365))
    cliente = random.choice(clientes)
    
    # Aseguramos que la sucursal tenga congruencia con su ciudad
    idx_sucursal = random.randint(0, len(sucursales)-1)
    sucursal = sucursales[idx_sucursal]
    ciudad = ciudades[idx_sucursal]
    estado = estados[idx_sucursal]
    
    vendedor = random.choice(vendedores)
    metodo_pago = random.choice(metodos_pago)
    
    # 1 a 3 productos por venta
    num_productos = random.randint(1, 3)
    for _ in range(num_productos):
        producto = random.choice(productos)
        cantidad = random.randint(1, 5)
        precio_unitario = producto[3]
        importe = cantidad * precio_unitario
        
        # Ojo con los nombres de las columnas, deben coincidir exacto con tu PDF (Página 18-19)
        fila = {
            "Categoria": producto[2],
            "Sucursal": sucursal,
            "Ciudad": ciudad,
            "Estado": estado,
            "Pais": "Mexico",
            "Metodo Pago": metodo_pago,
            "Cliente": cliente,
            "Vendedor": vendedor,
            "CodigoProducto": producto[0],
            "Producto": producto[1],
            "Documento": folio,
            "Fecha": fecha.strftime("%Y-%m-%d"),
            "Cantidad": cantidad,
            "PrecioUnitario": precio_unitario,
            "Importe": importe,
            "Subtotal": importe, # Simplificado para el ejemplo
            "Impuesto": importe * 0.16,
            "Total": importe * 1.16
        }
        datos.append(fila)
    folio_actual += 1

# Crear el DataFrame y guardarlo en Excel con la hoja específica
df = pd.DataFrame(datos)
with pd.ExcelWriter("DashBoard2021.xlsx") as writer:
    df.to_excel(writer, sheet_name="BaseDe Datos", index=False)

print("¡Magia completada! Se ha creado el archivo 'DashBoard2021.xlsx' con datos simulados.")