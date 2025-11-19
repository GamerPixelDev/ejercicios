#Ejercicio 9
#Crea una función ventas_destacadas(listaVentas) que:
#   -Filtre los productos cuyo importe total (precio * cantidad) sea mayor de 150€.
#   -Ordene esos productos de mayor a menor importe total.
#   -Devuelva solo la lista de nombres de productos en ese orden.

ventas = [
    {"producto": "Teclado", "precio": 25.99, "cantidad": 4}, #103.96
    {"producto": "Ratón", "precio": 14.50, "cantidad": 10}, #145
    {"producto": "Monitor", "precio": 199.99, "cantidad": 2}, #399.98
    {"producto": "USB 64GB", "precio": 9.99, "cantidad": 20}, #199.8
    {"producto": "Auriculares", "precio": 59.90, "cantidad": 3}, #179.7
]
def ventas_destacadas(listaVentas):
    importe = [i for i in listaVentas if (i["precio"] * i["cantidad"]) > 150]
    ordenados = sorted(importe, key=lambda o: (o["precio"] * o["cantidad"]), reverse=True)
    return [r["producto"] for r in ordenados]

print(ventas_destacadas(ventas))