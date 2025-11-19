#Ejercicio 10 – Filtrado y transformación de datos
#Crea una función pedidos_premium(listaPedidos) que:
#    -Seleccione solo los pedidos entregados.
#    -De esos, conserve únicamente los que tengan un importe mayor de 200.
#    -Los ordene por importe de mayor a menor.
#    -Devuelva una lista de strings con este formato exacto:
#       "Ana - 250.50€"
#Sí, con el símbolo del euro incluido.

pedidos = [
    {"cliente": "Ana", "importe": 250.50, "entregado": True},
    {"cliente": "Luis", "importe": 99.99, "entregado": False},
    {"cliente": "Carla", "importe": 310.00, "entregado": True},
    {"cliente": "Jorge", "importe": 150.00, "entregado": False},
    {"cliente": "Mara", "importe": 500.20, "entregado": True},
]

def pedidos_premium(listaPedidos):
    entregados = [e for e in listaPedidos if e["entregado"] and e["importe"] > 200]
    ordenados = sorted(entregados, key=lambda o: o["importe"], reverse=True)
    return [f"{r["cliente"]} - {r["importe"]}€" for r in ordenados]

print(pedidos_premium(pedidos))