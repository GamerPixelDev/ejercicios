#🧮 Ejercicio 25 – Dashboard de tu academia de cursos
#Tienes una academia online y quieres montar un “mini panel de control” a partir de una lista de matrículas.
#Parte A – dashboard_academia
#    Escribe una función:
#        def dashboard_academia(listaMatriculas):
#    que devuelva un diccionario con esta estructura:
#        "total_alumnos" → número de alumnos distintos.
#        "total_matriculas" → número total de matrículas (la longitud de la lista).
#        "ingresos_totales" → suma de precio de todas las matrículas (finalizadas o no; se supone que todas están cobradas).
#        "curso_top_ingresos" → el curso que más dinero ha generado (suma de precio por curso).
#        Puedes devolverlo, por ejemplo, como cadena tipo:
#            "Python básico — 480€"
#            o como un diccionario, lo que tú prefieras, pero que se entienda claro.
#        "alumno_mas_horas" → el alumno con más horas finalizadas. Aquí solo cuentan las horas (horas) de matrículas donde finalizado == True.
#        Igual que antes, puedes devolverlo como cadena tipo:
#            "Carla — 70h"
#            o en el formato que veas más cómodo.
#    La idea es que tengas que:
#        Contar alumnos distintos (set o diccionario, como prefieras).
#        Agrupar por curso para sumar ingresos.
#        Agrupar por alumno para sumar horas de cursos finalizados.
#        Sacar el máximo en cada agrupación.
#Parte B (opcional pero jugosa) – Ranking por curso
#    Si te ves con ganas, crea también:
#        def ranking_cursos_por_ingresos(listaMatriculas):
#    que devuelva una lista de cadenas, ordenadas de mayor a menor ingreso, por ejemplo:
#        [
#            "Python básico -> 480€",
#            "Data Science -> 200€",
#            "Power BI -> 150€",
#            "Excel avanzado -> 160€"
#        ]

matriculas = [
    {"alumno": "Ana",   "curso": "Python básico",   "horas": 30, "precio": 120, "finalizado": True},
    {"alumno": "Ana",   "curso": "Excel avanzado",  "horas": 20, "precio":  80, "finalizado": True},
    {"alumno": "Luis",  "curso": "Python básico",   "horas": 30, "precio": 120, "finalizado": False},
    {"alumno": "Carla", "curso": "Data Science",    "horas": 40, "precio": 200, "finalizado": True},
    {"alumno": "Carla", "curso": "Python básico",   "horas": 30, "precio": 120, "finalizado": True},
    {"alumno": "Jorge", "curso": "Excel avanzado",  "horas": 20, "precio":  80, "finalizado": False},
    {"alumno": "Mara",  "curso": "Power BI",        "horas": 25, "precio": 150, "finalizado": True},
    {"alumno": "Mara",  "curso": "Python básico",   "horas": 30, "precio": 120, "finalizado": True},
]

def dashboard_academia(listaMatriculas):
    academia = {}
    alumnos = set()
    ingreso_total = 0
    max_curso = None
    max_ingreso = -1
    max_alumno = None
    max_horas = -1
    for lm in listaMatriculas:
        alumnos.add(lm["alumno"])
        curso = lm["curso"]
        if curso not in academia:
            academia[curso] = {
                "matriculados": 0,
                "ingresos": 0,
                #"alumnos": [] #Esto ha sido un experimento mio, para ver si podía guardar una lista de nombres de los alumnos
            }
        academia[curso]["matriculados"] += 1
        academia[curso]["ingresos"] += lm["precio"]
        ingreso_total += lm["precio"]
        if academia[curso]["ingresos"] > max_ingreso:
            max_ingreso = academia[curso]["ingresos"]
            max_curso = curso
        if not lm["finalizado"]:
            continue
        #academia[curso]["alumnos"].append(lm["alumno"]) #Esto forma parte de mi experimento
        alumno = lm["alumno"]
        if alumno not in academia:
            academia[alumno] = {
                "total_horas": 0
            }
        academia[alumno]["total_horas"] += lm["horas"]
        if academia[alumno]["total_horas"] > max_horas:
            max_horas = academia[alumno]["total_horas"]
            max_alumno = alumno   
    academia["ingresos_totales"] = ingreso_total
    academia["top_curso_ingresos"] = max_curso
    academia["total_alumnos"] = len(alumnos)
    academia["top_horas_alumno"] = max_alumno
    return academia

#print(dashboard_academia(matriculas))

#Versión corregida
def dashboard_academia_2(listaMatriculas):
    alumnos = set()
    cursos = {}
    horas_alumnos = {}
    ingresos_totales = 0
    max_curso = None
    max_ingreso = -1
    max_alumno = None
    max_horas = -1
    for lm in listaMatriculas:
        alumnos.add(lm["alumno"])
        curso = lm["curso"]
        precio = lm["precio"]
        # Cursos
        if curso not in cursos:
            cursos[curso] = {"matriculados": 0, "ingresos": 0}
        cursos[curso]["matriculados"] += 1
        cursos[curso]["ingresos"] += precio
        ingresos_totales += precio
        if cursos[curso]["ingresos"] > max_ingreso:
            max_ingreso = cursos[curso]["ingresos"]
            max_curso = curso
        # Horas por alumno (solo finalizados)
        if not lm["finalizado"]:
            continue
        alumno = lm["alumno"]
        if alumno not in horas_alumnos:
            horas_alumnos[alumno] = 0
        horas_alumnos[alumno] += lm["horas"]
        if horas_alumnos[alumno] > max_horas:
            max_horas = horas_alumnos[alumno]
            max_alumno = alumno
    return {
        "total_alumnos": len(alumnos),
        "total_matriculas": len(listaMatriculas),
        "ingresos_totales": ingresos_totales,
        "curso_top_ingresos": f"{max_curso} — {max_ingreso}€",
        "alumno_mas_horas": f"{max_alumno} — {max_horas}h"
    }

#print(dashboard_academia_2(matriculas))

def ranking_cursos_por_ingresos(listaMatriculas):
    ranking = {}
    for lm in listaMatriculas:
        curso = lm["curso"]
        precio = lm["precio"]
        if curso not in ranking:
            ranking[curso] = 0
        ranking[curso] += precio
    ordenado = sorted(ranking.items(), key=lambda ro: ro[1], reverse=True)
    resultado = []
    for r in ordenado:
        curso = r[0]
        dinero = r[1]
        resultado.append(f"{curso} --> {dinero}€")
    return resultado

print(ranking_cursos_por_ingresos(matriculas))
        