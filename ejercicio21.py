#Ejercicio 21 – Clientes VIP de una tienda online
#Tu misión: función clientes_vip(listaCompras)
#   Solo cuentan las compras que no han sido devueltas (devuelto == False).
#   Para cada cliente, calcula:
#       El importe total gastado.
#       El número de compras válidas que ha hecho.
#   Consideramos cliente VIP si:
#       Ha gastado al menos 500 € en total.
#       Y tiene al menos 2 compras válidas.
#   La función debe devolver una lista de strings, con este formato:
#       "Ana — 620.0€ en 3 compras"
#   La lista debe venir ordenada de mayor a menor según el importe total gastado.
#   Extra (nivel “me gusta sufrir pero aprender”)
#   Si quieres rizar el rizo, añade también la categoría favorita del cliente, es decir, la categoría en la que más compras válidas ha hecho. Formato:
#       "Ana — 620.0€ en 3 compras — categoría favorita: tecnología"
#   En caso de empate entre categorías, puedes quedarte con cualquiera de las que empatan, no hace falta complicarse.

compras = [
    {"cliente": "Ana", "categoria": "tecnología", "importe": 250.0, "devuelto": False},
    {"cliente": "Ana", "categoria": "hogar", "importe": 120.0, "devuelto": False},
    {"cliente": "Ana", "categoria": "tecnología", "importe": 200.0, "devuelto": True},
    {"cliente": "Luis", "categoria": "ropa", "importe": 80.0, "devuelto": False},
    {"cliente": "Luis", "categoria": "tecnología", "importe": 300.0, "devuelto": False},
    {"cliente": "Carla", "categoria": "hogar", "importe": 150.0, "devuelto": False},
    {"cliente": "Carla", "categoria": "hogar", "importe": 200.0, "devuelto": False},
    {"cliente": "Carla", "categoria": "tecnología", "importe": 220.0, "devuelto": False},
    {"cliente": "Jorge", "categoria": "ropa", "importe": 60.0, "devuelto": True},
    {"cliente": "Jorge", "categoria": "ropa", "importe": 90.0, "devuelto": False},
    {"cliente": "Mara", "categoria": "tecnología", "importe": 400.0, "devuelto": False},
    {"cliente": "Mara", "categoria": "hogar", "importe": 50.0, "devuelto": False},
]

def clientes_vip(listaCompras):
    comprasAna = [ca for ca in listaCompras
                            if ca['cliente'] == 'Ana'
                        ]
    nombreAna = comprasAna[0]['cliente']
    totalComprasAna = 0
    comprasValidasAna = 0
    clienteVipAna = False
    for ca in comprasAna:
        if not ca['devuelto']:
            totalComprasAna = totalComprasAna + ca['importe']
            comprasValidasAna += 1
    if totalComprasAna >= 500 and comprasValidasAna >= 2:
        clienteVipAna = True
    totalAna = f"{nombreAna} - {totalComprasAna} en {comprasValidasAna} compras"
    resumen = []
    resumen.append(totalAna)
    return resumen

print(clientes_vip(compras))