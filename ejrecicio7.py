#Ejercicio 7: “Los empleados productivos”
#Crea una función empleados_productivos que:
#   -Calcule la productividad de cada empleado con la fórmula:
#       -productividad = proyectos / horas
#   -Se quede solo con empleados cuya productividad sea mayor o igual que 0.05.
#   -Devuelva una lista de nombres, ordenados de mayor a menor productividad.

empleados = [
    {"nombre": "Ana", "horas": 38, "proyectos": 2},
    {"nombre": "Luis", "horas": 42, "proyectos": 1},
    {"nombre": "Carla", "horas": 45, "proyectos": 3},
    {"nombre": "Jorge", "horas": 30, "proyectos": 1},
    {"nombre": "Mara", "horas": 50, "proyectos": 4},
]

def empleados_productivos(listaEmpleados):
    productivos = [p for p in listaEmpleados if (p["proyectos"] / p["horas"]) >= 0.05]
    ordenados = sorted(productivos, key=lambda o: (o["proyectos"] / o["horas"]), reverse=True)
    return [r["nombre"] for r in ordenados]

print(empleados_productivos(empleados))