#Ejercicio 3 – Filtrar, transformar y ordenar diccionarios
#Crear una función llamada ranking_activos(listaJugadores) que:
#Filtre solo los jugadores activos.
#Ordene esos jugadores activos por puntuación de mayor a menor.
#Transforme la lista para devolver solo un listado de cadenas con el formato:

jugadores = [
    {"nombre": "Ana", "puntuacion": 120, "activo": True},
    {"nombre": "Luis", "puntuacion": 95, "activo": False},
    {"nombre": "Carla", "puntuacion": 180, "activo": True},
    {"nombre": "Jorge", "puntuacion": 70, "activo": True},
    {"nombre": "Mara", "puntuacion": 130, "activo": False},
]

def ranking_activos(listaJugadores):
    activos = [a for a in listaJugadores if a["activo"] == True]
    ordenados = sorted(activos, key=lambda a: a["puntuacion"], reverse=True)
    return [f"{j["nombre"]} - {j["puntuacion"]} puntos" for j in ordenados]

print(ranking_activos(jugadores))