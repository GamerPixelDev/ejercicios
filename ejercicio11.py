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

#Ejercicio 11B – El criba-locura de vehículos
#Tienes la misma lista de vehículos, pero ahora la función se llama
#vehiculos_premium(listaVehiculos) y debe cumplir TODAS estas condiciones a la vez:
#    Solo queremos vehículos NO vendidos.
#    Año entre 2016 y 2020, ambos incluidos.
#    Menos de 120.000 km, pero OJO:
#    Si el vehículo tiene más de 80.000 km, entonces solo pasa el filtro si el año es 2019 o 2020. (Esto es la trampa lógica típica)
#    Debes ordenarlos primero por año descendente (más nuevos primero) y si empatan, por km ascendente (menos km primero).
#    Devuelve strings con formato:
#        "MODELO – AÑO – X km"

def vehiculos_premium(listaVehiculos):
    nVendidos = [nv for nv in listaVehiculos
                    if not nv["vendido"]
                    and 2016 <= nv["año"] <= 2020
                    and ((nv["km"] <= 80000)
                            or (nv["km"] > 80000 and nv["año"] >= 2019)
                        )
                ]
    ordenados = sorted(nVendidos, key=lambda o: (o["año"], o["km"]))
    return [f"{r['modelo']} - {r['año']} - {r['km']}km" for r in ordenados]

print(vehiculos_premium(vehiculos))