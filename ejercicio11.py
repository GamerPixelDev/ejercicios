#Ejercicio 11 – Filtrado múltiple y transformación
#Tienes una lista de vehículos. Cada uno tiene:
#    modelo (str)
#    año (int)
#    km (int)
#    vendido (bool)
#Tu objetivo es crear una función llamada vehiculos_seleccionados(listaVehiculos) que:
#    Se quede solo con los vehículos NO vendidos.
#    Que además sean del año 2015 o más nuevos.
#    Y tengan menos de 100.000 km.
#    Ordene la lista resultante por km ascendente (menos km → primero)
#    Devuelva una lista de strings en formato:
#        "MODELO (AÑO) - X km"

vehiculos = [
    {"modelo": "Ford Fiesta", "año": 2012, "km": 85000, "vendido": False},
    {"modelo": "Seat León", "año": 2018, "km": 45000, "vendido": False},
    {"modelo": "Audi A3", "año": 2016, "km": 120000, "vendido": False},
    {"modelo": "Toyota Corolla", "año": 2019, "km": 30000, "vendido": True},
    {"modelo": "Renault Clio", "año": 2017, "km": 90000, "vendido": False},
]

def vehiculos_seleccionados(listaVehiculos):
    noVendidos = [nv for nv in listaVehiculos if nv ["vendido"] == False and nv["año"] >= 2015 and nv["km"] < 100000]
    ordenados = sorted(noVendidos, key=lambda o: o["km"])
    return [f"{r['modelo']} ({r['año']}) - {r['km']}km" for r in ordenados]

print(vehiculos_seleccionados(vehiculos))