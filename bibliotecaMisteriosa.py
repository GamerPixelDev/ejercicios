#Ejercicio 1 – “La biblioteca misteriosa” (Python)
#Tienes una lista de diccionarios que representan libros. Cada libro tiene:
# -título
# -autor
# -año
# -número de páginas
#El objetivo es escribir una función que:
#Reciba esta lista.
#Devuelva solo los libros publicados después del año 2000.
#Ordenados de mayor a menor número de páginas.
#Y que el resultado final sea una lista de los títulos, no de los diccionarios completos.

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

#Función compacta
def filtrar_y_ordenar_OP(libros):
    filtrados = [l for l in libros if l["anio"] > 2000]
    ordenados = sorted(filtrados, key=lambda l: l["paginas"], reverse=True)
    return [l["titulo"] for l in ordenados]

print(filtrar_y_ordenar(libros))