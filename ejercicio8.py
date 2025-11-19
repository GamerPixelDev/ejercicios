#Ejercicio 8
#Debes crear una función alumnos_sobresalientes_jovenes(listaAlumnos) que:
#   -Se quede solo con los alumnos que tengan más de 8 de nota.
#   -De esos, filtre los que tengan 20 años o menos.
#   -Los ordene por nota de mayor a menor.
#   -Devuelva una lista solo con los nombres.

alumnos = [
    {"nombre": "Ana", "nota": 7.5, "edad": 20},
    {"nombre": "Luis", "nota": 4.8, "edad": 22},
    {"nombre": "Carla", "nota": 9.1, "edad": 19},
    {"nombre": "Jorge", "nota": 6.0, "edad": 21},
    {"nombre": "Mara", "nota": 8.4, "edad": 20},
]

def alumnos_sobresalientes(listaAlumnos):
    alumn = [a for a in listaAlumnos if a["nota"] > 8 and a["edad"] <= 20]
    ordenados = sorted(alumn, key=lambda o: o["nota"], reverse=True)
    return [r["nombre"] for r in ordenados]

print(alumnos_sobresalientes(alumnos))