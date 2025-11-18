libros = [
    {"titulo": "El viaje del norte", "autor": "M. Ruiz", "anio": 1998, "paginas": 320},
    {"titulo": "Sombras de acero", "autor": "L. Bronte", "anio": 2005, "paginas": 410},
    {"titulo": "Códigos en el viento", "autor": "K. Moran", "anio": 2012, "paginas": 280}, 
]

def filtrar_y_ordenar(libros):
    guardar = []
    titulos = []
    for u in libros:
        if u["anio"] > 2000:
            guardar.append(u)
    guardar.sort(key=lambda libro: libro['paginas'], reverse=True)
    for g in guardar:
        titulos.append(g["titulo"])
    return titulos

print(filtrar_y_ordenar(libros))