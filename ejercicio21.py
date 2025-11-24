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

def cliente_vip_2(listaCompras):
    #Acumulamos los datos por cliente (solo compras no devueltas)
    resumen = {}
    favTec = 0
    favRop = 0
    favHog = 0
    for lc in listaCompras:
        if lc['devuelto']:
            continue #Aquí se ignoran devoluciones
        nombre = lc['cliente']
        importe = lc['importe']
        favorito = lc['categoria']
        if nombre not in resumen:
            resumen[nombre] = {"total": 0.0, "compras": 0, "favorito": None}
        resumen[nombre]["total"] += importe
        resumen[nombre]["compras"] += 1
        if favorito == "tecnología":
            favTec += 1
        elif favorito == "ropa":
            favRop += 1
        else:
            favHog +=1
        resultadoFav =  max(favTec, favRop, favHog)
        if resultadoFav == favTec:
            resumen[nombre]["favorito"] = "tecnología"
        elif resultadoFav == favRop:
            resumen[nombre]["favorito"] = "ropa"
        else:
            resumen[nombre]["favorito"] = "hogar"
        #Filtramos los clientes VIPs
    vips = []
    for nombre, datos in resumen.items():
        total = datos["total"]
        compras = datos["compras"]
        favorito = datos["favorito"]
        if total >= 500 and compras >= 2:
            vips.append((nombre, total, compras, favorito))
    #Ordenamos los clientes de mayor a menor total gastado
    vips.sort(key=lambda vo: -vo[1])
    #Damos formato a la salida
    resultado = [f"{nombre} — {total}€ en {compras} compras — categoría favorita: {favorito}"
                    for (nombre, total, compras, favorito) in vips
                ]
        
    return resultado, favTec, favRop, favHog

print(cliente_vip_2(compras))

def clientes_vip_3(listaCompras):
    resumen = []
    # 1. Sacamos el conjunto de nombres de clientes
    clientes = {c["cliente"] for c in listaCompras}
    # 2. Para cada cliente calculamos sus estadísticas
    for nombre in clientes:
        # compras de ese cliente que NO han sido devueltas
        compras_cliente = [
            c for c in listaCompras
            if c["cliente"] == nombre and not c["devuelto"]
        ]
        total = sum(c["importe"] for c in compras_cliente)
        compras_validas = len(compras_cliente)
        # 3. ¿Es VIP?
        if total >= 500 and compras_validas >= 2:
            resumen.append((nombre, total, compras_validas))
    # 4. Ordenamos de mayor a menor por total gastado
    resumen_ordenado = sorted(resumen, key=lambda t: t[1], reverse=True)
    # 5. Formateamos la salida
    return [
        f"{nombre} — {total}€ en {compras} compras"
        for (nombre, total, compras) in resumen_ordenado
    ]

print(clientes_vip_3(compras))