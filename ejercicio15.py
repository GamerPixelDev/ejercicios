#Ejercicio 15 — “Ventas sospechosamente altas”
#Tienes una lista de ventas donde cada venta es un diccionario con:
#   "producto": nombre del producto
#   "precio_unitario"
#   "cantidad"
#   "devoluciones" (número de unidades devueltas)
#La empresa quiere detectar ventas sospechosamente altas, que son aquellas que:
#   Tienen un importe total (precio_unitario * cantidad) mayor de 500 €.
#   Y además tienen 0 devoluciones.
#   Y además el nombre del producto empieza con una letra del rango A–M (incluyendo ambas).
#Tu función debe devolver una lista de strings con el formato:
#   "Producto — ImporteTotal€"
#Ordenados de mayor a menor importe.

ventas = [
    {"producto": "Monitor UltraHD", "precio_unitario": 320, "cantidad": 2, "devoluciones": 0},
    {"producto": "Alfombrilla Pro", "precio_unitario": 15, "cantidad": 1, "devoluciones": 0},
    {"producto": "Mochila Gaming", "precio_unitario": 80, "cantidad": 7, "devoluciones": 1},
    {"producto": "Auriculares MaxSound", "precio_unitario": 120, "cantidad": 5, "devoluciones": 0},
    {"producto": "Teclado Mecánico", "precio_unitario": 90, "cantidad": 6, "devoluciones": 0},
]

def ventas_sospechosas(listaVentas):
    sospechosos = [s for s in listaVentas
                    if  (s["precio_unitario"] * s["cantidad"]) > 500
                    and s["devoluciones"] == 0
                    and "A" <= s["producto"][0].upper() <= "M"
                ]
    ordenados = sorted(sospechosos, key=lambda o: (-o["precio_unitario"] * o["cantidad"]))
    return [f"{r['producto']} - {r['precio_unitario'] * r['cantidad']}€" for r in ordenados]

print(ventas_sospechosas(ventas))