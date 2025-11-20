#Ejercicio 13 — Inventario maldito
#Tienes una lista de objetos de un almacén. Cada objeto tiene:
#   nombre
#   categoria (por ejemplo: "electrónica", "ropa", "alimentos")
#   precio
#   stock
#   descatalogado (True/False)
#Crea una función llamada electro_top(inventario) que:
#   Seleccione SOLO los productos de categoría “electrónica”.
#   Excluya los que estén descatalogados.
#   Excluya los que tengan stock 0.
#   Ordene los resultados por precio descendente.
#   Devuelva una lista de strings tipo:
#       "Portátil Gamer - 1200€ (stock: 5)"

inventario = [
    {"nombre": "Portátil Gamer", "categoria": "electrónica", "precio": 1200, "stock": 5, "descatalogado": False},
    {"nombre": "Camiseta Negra", "categoria": "ropa", "precio": 15, "stock": 50, "descatalogado": False},
    {"nombre": "Televisor 4K", "categoria": "electrónica", "precio": 700, "stock": 0, "descatalogado": True},
    {"nombre": "Auriculares Pro", "categoria": "electrónica", "precio": 180, "stock": 12, "descatalogado": False},
    {"nombre": "Zapatillas Running", "categoria": "ropa", "precio": 75, "stock": 3, "descatalogado": False},
    {"nombre": "Café Premium", "categoria": "alimentos", "precio": 9, "stock": 100, "descatalogado": False},
]

def electro_top(listaInventario):
    itemElectronic = [ie for ie in listaInventario
                        if ie["categoria"] == "electrónica"
                        and not ie["descatalogado"]
                        and ie["stock"] > 0
                    ]
    ordenados = sorted(itemElectronic, key=lambda o: -o["precio"])
    return [f"{r['nombre']} - {r['precio']}€ (stock: {r['stock']})" for r in ordenados]

print(electro_top(inventario))

#Ejercicio 13B — Inventario maldito, segunda fase
#Filtra exactamente como en el 13, PERO añade estas reglas nuevas:
#   Regla 1 — Solo queremos los 3 más caros.
#       Si hay menos de 3, devuelves los que haya.
#   Regla 2 — En caso de empate de precio, desempata por orden alfabético.
#   Regla 3 — Si después de filtrar no queda NINGÚN producto válido, devuelve la cadena:
#       "No hay productos electrónicos disponibles."
#Devuelve una lista de strings así:
#   "Portátil Gamer — 1200€ — stock 5"

def item_electro(listaInventario):
    itemElectronico = [ie for ie in listaInventario
                        if ie["categoria"] == "electrónica"
                        and not ie["descatalogado"]
                        and ie["stock"] > 0
                    ]
    if not itemElectronico:
        return "No hay productos electrónicos disponibles."
    ordenados = sorted(itemElectronico, key=lambda o: (-o["precio"], o["nombre"]))
    nuevaLista = ordenados[:3]
    return [f"{r['nombre']} — {r['precio']}€ — stock {r['stock']}" for r in nuevaLista]