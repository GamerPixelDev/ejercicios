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
    resumen = []
    #Vemos si Ana es cliente VIP
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
    if clienteVipAna:
        resumen.append(totalAna)
    #Vemos si Luis es cliente VIP
    comprasLuis = [cl for cl in listaCompras
                            if cl['cliente'] == 'Luis'
                        ]
    nombreLuis = comprasLuis[0]['cliente']
    totalComprasLuis = 0
    comprasValidasLuis = 0
    clienteVipLuis = False
    for cl in comprasLuis:
        if not cl['devuelto']:
            totalComprasLuis = totalComprasLuis + cl['importe']
            comprasValidasLuis += 1
    if totalComprasLuis >= 500 and comprasValidasLuis >= 2:
        clienteVipLuis = True
    totalLuis = f"{nombreLuis} - {totalComprasLuis} en {comprasValidasLuis} compras"
    if clienteVipLuis:
        resumen.append(totalLuis)
    #Vemos si Carla es cliente VIP
    comprasCarla = [cc for cc in listaCompras
                            if cc['cliente'] == 'Carla'
                        ]
    nombreCarla = comprasCarla[0]['cliente']
    totalComprasCarla = 0
    comprasValidasCarla = 0
    clienteVipCarla = False
    for cc in comprasCarla:
        if not cc['devuelto']:
            totalComprasCarla = totalComprasCarla + cc['importe']
            comprasValidasCarla += 1
    if totalComprasCarla >= 500 and comprasValidasCarla >= 2:
        clienteVipCarla = True
    totalCarla = f"{nombreCarla} - {totalComprasCarla} en {comprasValidasCarla} compras"
    if clienteVipCarla:
        resumen.append(totalCarla)
    #Vemos si Jorge es cliente VIP
    comprasJorge = [cj for cj in listaCompras
                            if cj['cliente'] == 'Jorge'
                        ]
    nombreJorge = comprasJorge[0]['cliente']
    totalComprasJorge = 0
    comprasValidasJorge = 0
    clienteVipJorge = False
    for cj in comprasJorge:
        if not cj['devuelto']:
            totalComprasJorge = totalComprasJorge + cj['importe']
            comprasValidasJorge += 1
    if totalComprasJorge >= 500 and comprasValidasJorge >= 2:
        clienteVipJorge = True
    totalJorge = f"{nombreJorge} - {totalComprasJorge} en {comprasValidasJorge} compras"
    if clienteVipJorge:
        resumen.append(totalJorge)
    #Vemos si Mara es cliente VIP
    comprasMara = [cm for cm in listaCompras
                            if cm['cliente'] == 'Mara'
                        ]
    nombreMara = comprasMara[0]['cliente']
    totalComprasMara = 0
    comprasValidasMara = 0
    clienteVipMara = False
    for cm in comprasMara:
        if not cm['devuelto']:
            totalComprasMara = totalComprasMara + cm['importe']
            comprasValidasMara += 1
    if totalComprasMara >= 500 and comprasValidasMara >= 2:
        clienteVipMara = True
    totalMara = f"{nombreMara} - {totalComprasMara} en {comprasValidasMara} compras"
    if clienteVipMara:
        resumen.append(totalMara)
    return resumen

print(clientes_vip(compras))