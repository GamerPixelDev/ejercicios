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
    resumen = {}
    alumnos = set() #Con set() es como una lista pero cada elemento solo puede aparecer una vez
    cursosFinalizado = 0
    totalNotas = 0.0
    for lm in listaMatriculas:
        alumnos.add(lm['alumno'])
        if not lm['finalizado']:
            continue
        cursosFinalizado += 1
        totalNotas = totalNotas + lm['nota']

    totalAlumnos = len(alumnos)
        
    return totalAlumnos, cursosFinalizado, totalNotas

print(resumen_academico(matriculas))