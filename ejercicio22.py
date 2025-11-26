#Ejercicio 22 – Resumen académico por alumno
#Crea una función resumen_academico(listaMatriculas) que devuelva un diccionario con este formato:
#   {
#       "total_alumnos": X,            --> número de alumnos distintos
#       "total_cursos_finalizados": Y, --> cuántas matrículas tienen finalizado == True
#       "nota_media_global": Z,        --> media de todas las notas de cursos finalizados (redondeada a 2 decimales)
#       "top_alumno": "Nombre — media" --> el alumno con mejor media de nota en cursos finalizados
#   }
#Detalles importantes:
#   Las matrículas donde finalizado == False no cuentan para notas ni para cursos finalizados.
#   nota_media_global es la media de todas las notas de cursos finalizados.
#   Para top_alumno, calcula la media de las notas de cada alumno (solo cursos finalizados) y devuelve una cadena tipo:
#       "Carla — 9.0"
#   Si la lista viene vacía o no hay ningún curso finalizado, la función puede devolver {}.

matriculas = [
    {"alumno": "Ana", "curso": "Python básico", "horas": 30, "finalizado": True,  "nota": 8.5},
    {"alumno": "Ana", "curso": "Excel avanzado", "horas": 20, "finalizado": True,  "nota": 7.0},
    {"alumno": "Luis", "curso": "Python básico", "horas": 30, "finalizado": False, "nota": None},
    {"alumno": "Carla", "curso": "Bases de datos", "horas": 40, "finalizado": True, "nota": 9.2},
    {"alumno": "Carla", "curso": "Python básico", "horas": 30, "finalizado": True, "nota": 8.8},
    {"alumno": "Jorge", "curso": "Excel avanzado", "horas": 20, "finalizado": True, "nota": 5.5},
]

def resumen_academico(listaMatriculas):
    if not listaMatriculas:
        return {}
    alumnos = set()
    cursos_finalizados = 0
    suma_notas_global = 0.0
    contador_notas = 0
    # Aquí guardamos TODAS las notas por alumno
    # Ej: {"Ana": [8.5, 7.0], "Carla": [9.2, 8.8], "Jorge": [5.5]}
    notas_por_alumno = {}
    for lm in listaMatriculas:
        alumnos.add(lm["alumno"])
        if not lm["finalizado"]:
            continue  # ignoramos los cursos no finalizados
        cursos_finalizados += 1
        nota = lm["nota"]
        suma_notas_global += nota
        contador_notas += 1
        nombre = lm["alumno"]
        if nombre not in notas_por_alumno:
            notas_por_alumno[nombre] = []
        notas_por_alumno[nombre].append(nota)
    # Si no hay ningún curso finalizado, devolvemos diccionario vacío
    if contador_notas == 0:
        return {}
    nota_media_global = round(suma_notas_global / contador_notas, 2)
    # ---- Cálculo de top_alumno ----
    mejor_nombre = None
    mejor_media = -1
    for nombre, lista_notas in notas_por_alumno.items():
        media = sum(lista_notas) / len(lista_notas)
        if media > mejor_media:
            mejor_media = media
            mejor_nombre = nombre
    top_alumno = f"{mejor_nombre} — {round(mejor_media, 1)}"
    resumen = {
        "total_alumnos": len(alumnos),
        "total_cursos_finalizados": cursos_finalizados,
        "nota_media_global": nota_media_global,
        "top_alumno": top_alumno
    }
    return resumen, notas_por_alumno

print(resumen_academico(matriculas))