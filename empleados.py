#Ejercicio 5 — Filtrar empleados y devolverlos ordenados
#Tienes una lista de empleados, cada uno con nombre, salario y departamento.
#Haz una función empleados_marketing_bienpagados que:
#   -Se quede solo con los empleados del departamento "Marketing".
#   -De esos, filtre solo los que ganen más de 2000.
#   -Devuelva una lista con los nombres, ordenados de mayor a menor salario.

empleados = [
    {"nombre": "Ana", "salario": 2500, "departamento": "Marketing"},
    {"nombre": "Luis", "salario": 1800, "departamento": "Ventas"},
    {"nombre": "Carla", "salario": 2200, "departamento": "Marketing"},
    {"nombre": "Jorge", "salario": 1950, "departamento": "Marketing"},
    {"nombre": "Mara", "salario": 3000, "departamento": "Ventas"},
]
def empleado_marketing_bienpagados(listaEmpleados):
    marketing = [m for m in listaEmpleados
                    if m["departamento"] == "Marketing" and m["salario"] > 2000
                ]
    ordenados = sorted(marketing, key=lambda o: o["salario"], reverse=True)
    return[r["nombre"] for r in ordenados]

print(empleado_marketing_bienpagados(empleados))