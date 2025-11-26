#Ejercicio 23 — Resumen por curso
#Para cada curso tienes que calcular:
#    matriculados → número total de matrículas de ese curso (cada entrada en la lista cuenta como una matrícula, no hace falta eliminar duplicados de alumno).
#    finalizados → cuántas de esas matrículas tienen finalizado == True.
#    nota_media → media de nota solo de las matrículas finalizadas con nota distinta de None.
#    Redondea a 1 decimal con round(..., 1).
#    Si no hay ninguna nota válida, pon None.
#    tasa_finalizacion → porcentaje de matrículas finalizadas:
#        tasa = (finalizados / matriculados) * 100 también redondeada a 1 decimal.
#   que devuelva un diccionario de resumen por curso con este formato:
#       {
#           "Python básico": {
#               "matriculados": ...,
#               "finalizados": ...,
#               "nota_media": ...,
#               "tasa_finalizacion": ...
#            },
#            "Excel avanzado": {
#                "matriculados": ...,
#                "finalizados": ...,
#                "nota_media": ...,
#                "tasa_finalizacion": ...
#            },
#         ...
#       }

matriculas = [
    {"alumno": "Ana",   "curso": "Python básico",  "horas": 30, "finalizado": True,  "nota": 8.5},
    {"alumno": "Ana",   "curso": "Excel avanzado","horas": 20, "finalizado": True,  "nota": 7.0},
    {"alumno": "Luis",  "curso": "Python básico",  "horas": 30, "finalizado": False, "nota": None},
    {"alumno": "Carla", "curso": "Bases de datos", "horas": 40, "finalizado": True,  "nota": 9.2},
    {"alumno": "Carla", "curso": "Python básico",  "horas": 30, "finalizado": True,  "nota": 9.0},
    {"alumno": "Jorge", "curso": "Excel avanzado","horas": 20, "finalizado": False, "nota": None},
]

def resumen_cursos(listaMatriculas):
    resumen = {}
    cursos = set()
    cursoPython = 0
    notaPython = 0.0
    finalPython = 0
    cursoExcel = 0
    notaExcel = 0.0
    finalExcel = 0
    cursoBd = 0
    notaBd = 0.0
    finalBd = 0
    sum_notas = 0.0
    num_notas = 0
    for lm in listaMatriculas:
        cursos.add(lm['curso'])
        if lm['curso'] == "Python básico":
            cursoPython += 1
            if lm['finalizado']:
                notaPython += lm['nota']
                finalPython += 1
        elif lm['curso'] == "Excel avanzado":
            cursoExcel += 1
            if lm['finalizado']:
                notaExcel += lm['nota']
                finalExcel += 1
        else:
            cursoBd +=1
            if lm['finalizado']:
                notaBd += lm['nota']
                finalBd += 1
        if not lm['finalizado']:
            continue
        sum_notas = sum_notas + lm['nota']
        num_notas += 1
    mediaPython = round(notaPython / finalPython, 1)
    mediaExcel = round(notaExcel / finalExcel, 1)
    mediaBd = round(notaBd / finalBd, 1)

    return mediaPython, mediaExcel, mediaBd

print(resumen_cursos(matriculas))