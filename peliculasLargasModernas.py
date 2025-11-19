#Ejercicio 4 — Filtrar, transformar y ordenar
#Crea una función llamada peliculas_largas_modernas(listaPeliculas) que:
#   -Filtre solo las películas:
#       -con más de 100 minutos,
#       -y de estreno posterior al año 2000.
#   -Ordene las películas resultantes por duración de mayor a menor.
#   -Devuelva una lista solo con los títulos, en ese orden.

peliculas = [
    {"titulo": "Horizonte Azul", "anio": 1999, "duracion": 120},
    {"titulo": "La Sombra Roja", "anio": 2004, "duracion": 95},
    {"titulo": "Código Estelar", "anio": 2018, "duracion": 143},
    {"titulo": "El Ultimo Refugio", "anio": 2007, "duracion": 102},
    {"titulo": "Ecos del Pasado", "anio": 1995, "duracion": 110},
]
def peliculas_largas_modernas(listaPeliculas):
    pelis = [p for p in listaPeliculas if p["duracion"] > 100]
    masPelis = [m for m in pelis if m["anio"] > 2000]
    ordenadas = sorted(masPelis, key=lambda o: o["duracion"], reverse=True)
    return [r["titulo"] for r in ordenadas]

#Versión más compacta
def peliculas_largas_modernas_V2(listaPeliculas):
    pelis = [p for p in listaPeliculas if p["duracion"] > 100 and p["anio"] > 2000]
    ordenadas = sorted(pelis, key=lambda o: o["duracion"], reverse=True)
    return [r["titulo"] for r in ordenadas]

print(peliculas_largas_modernas(peliculas))
print(peliculas_largas_modernas_V2(peliculas))