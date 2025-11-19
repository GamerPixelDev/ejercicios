#EJERCICIO 2
#Haz una función llamada productos_disponibles_ordenados que:
#Filtre únicamente los productos cuyo stock sea mayor que 0.
#Ordene esos productos por precio de menor a mayor.
#Devuelva una lista con los nombres de los productos en ese orden.

productos = [
    {"nombre": "Teclado", "precio": 25.99, "stock": 12},
    {"nombre": "Ratón", "precio": 14.50, "stock": 0},
    {"nombre": "Monitor", "precio": 199.99, "stock": 5},
    {"nombre": "USB 64GB", "precio": 9.99, "stock": 34},
    {"nombre": "Auriculares", "precio": 59.90, "stock": 3},
]

def productos_disponibles_ordenados(listaProductos):
    stock = [s for s in listaProductos if s["stock"] > 0]
    ordenados = sorted(stock, key=lambda s: s["precio"], reverse=False)
    return [s["nombre"] for s in ordenados]

print(productos_disponibles_ordenados(productos))