#Ejercicio 24: “Lectores voraces”.
#Que devuelva un diccionario donde:
#    La clave sea el nombre del usuario ("Ana", "Luis", etc.)
#    El valor sea otro diccionario con estos datos, pero solo contando los préstamos devueltos (devuelto == True):
#        libros_leidos: número de libros devueltos por ese usuario.
#        paginas_leidas: suma de páginas de esos libros devueltos.
#        calificacion_media: media de calificacion de sus libros devueltos que tengan calificación distinta de None.
#    Si no tiene ninguna calificación válida, calificacion_media será None.
#    Ejemplo de forma aproximada del resultado (no te fíes de los números, son inventados):
#        {
#            "Ana": {
#                "libros_leidos": 2,
#                "paginas_leidas": 730,
#                "calificacion_media": 8.8
#            },
#            "Luis": {
#                "libros_leidos": 1,
#                "paginas_leidas": 290,
#                "calificacion_media": 7.0
#            },
#            ...
#        }
#    Extra (opcional, nivel picante 🌶️)
#        Si te ves con ganas, dentro de la misma función, después de construir el resumen, calcula también el usuario que más páginas ha leído
#        (paginas_leidas más alto) y haz que la función devuelva una tupla:
#            resumen, top_lector
#        donde top_lector sea el nombre del usuario con más páginas leídas.

prestamos = [
    {"usuario": "Ana",   "titulo": "El viaje de los mundos",   "genero": "fantasía",  "paginas": 420, "devuelto": True,  "calificacion": 8.5},
    {"usuario": "Ana",   "titulo": "Datos y dragones",         "genero": "tecnología","paginas": 310, "devuelto": True,  "calificacion": 9.0},
    {"usuario": "Luis",  "titulo": "Minimalismo digital",      "genero": "ensayo",    "paginas": 250, "devuelto": False, "calificacion": None},
    {"usuario": "Luis",  "titulo": "Sombras en la red",        "genero": "thriller",  "paginas": 290, "devuelto": True,  "calificacion": 7.0},
    {"usuario": "Carla", "titulo": "El bosque eterno",         "genero": "fantasía",  "paginas": 380, "devuelto": True,  "calificacion": 9.2},
    {"usuario": "Carla", "titulo": "Códigos y hechizos",       "genero": "fantasía",  "paginas": 450, "devuelto": True,  "calificacion": 8.8},
    {"usuario": "Jorge", "titulo": "Productividad sin humo",   "genero": "ensayo",    "paginas": 200, "devuelto": True,  "calificacion": None},
    {"usuario": "Mara",  "titulo": "Crónicas del vacío",       "genero": "ciencia ficción", "paginas": 500, "devuelto": False, "calificacion": None},
]

def resumen_lectores(listaPrestamos):
    resumen = {}
    for lp in listaPrestamos:
        user = lp["usuario"]
        if user not in resumen:
            resumen[user] = {
                "libros_leidos": 0,
                "paginas_leidas": 0,
                "total_cal": 0.0,
                "sum_cal": 0 
            }
        resumen[user]["libros_leidos"] += 1
        resumen[user]["paginas_leidas"] += lp["paginas"]
        if lp["devuelto"] and lp["calificacion"] is not None:
            resumen[user]["total_cal"] += lp["calificacion"]
            resumen[user]["sum_cal"] += 1
    user_max = None
    paginas_max = -1
    for user, datos in resumen.items():
        calificacionMedia = datos["total_cal"] / datos["sum_cal"] if datos["sum_cal"] > 0 else None
        datos["calificacion_media"] = calificacionMedia
        del(datos["total_cal"], datos["sum_cal"])
        if paginas_max < datos["paginas_leidas"]:
            paginas_max = datos["paginas_leidas"]
            user_max = user
    top_lector = f"Usuario que más páginas ha leído es: {user_max}"
        
    return resumen, top_lector

print(resumen_lectores(prestamos))