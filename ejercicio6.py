#Ejercicio 6
#Escribe una función llamada mejores_sci_fi que:
#   -Se quede solo con las películas de género "Sci-Fi".
#   -De esas, filtre únicamente las que tengan puntuación mayor o igual a 8.0.
#   -Devuelva una lista de títulos ordenados por puntuación de mayor a menor.

peliculas = [
    {"titulo": "Luz de Medianoche", "anio": 2010, "genero": "Drama", "puntuacion": 7.8},
    {"titulo": "Galaxia Roja", "anio": 2019, "genero": "Sci-Fi", "puntuacion": 8.5},
    {"titulo": "Sombras del Ayer", "anio": 2004, "genero": "Drama", "puntuacion": 6.9},
    {"titulo": "Ruptura Inminente", "anio": 2021, "genero": "Acción", "puntuacion": 7.2},
    {"titulo": "Código Fantasma", "anio": 2017, "genero": "Sci-Fi", "puntuacion": 8.1},
]

def mejores_sci_fi(listaPeliculas):
    pelis = [p for p in listaPeliculas
                if p["genero"] == "Sci-Fi" and p["puntuacion"] >= 8
            ]
    ordenadas = sorted(pelis, key=lambda o: o["puntuacion"], reverse=True)
    return [o["titulo"] for o in ordenadas]

print(mejores_sci_fi(peliculas))