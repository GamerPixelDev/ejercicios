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
    mediaPython = round(notaPython / finalPython, 1) if finalPython > 0 else None
    mediaExcel = round(notaExcel / finalExcel, 1) if finalExcel > 0 else None
    mediaBd = round(notaBd / finalBd, 1) if finalBd > 0 else None
    tasaPython = round((finalPython / cursoPython) * 100, 1) if cursoPython > 0 else None
    tasaExcel = round((finalExcel / cursoExcel) * 100, 1) if cursoExcel > 0 else None
    tasaBd = round((finalBd / cursoBd) * 100, 1) if cursoBd > 0 else None
    resumen["Python básico"] = {
        "matriculados": cursoPython,
        "finalizados": finalPython,
        "nota_media": mediaPython, 
        "tasa_finalizacion": tasaPython
    }
    resumen["Excel avanzado"] = {
        "matriculados": cursoExcel,
        "finalizados": finalExcel,
        "nota_media": mediaExcel, 
        "tasa_finalizacion": tasaExcel
    }
    resumen["Bases de datos"] = {
        "matriculados": cursoBd,
        "finalizados": finalBd,
        "nota_media": mediaBd, 
        "tasa_finalizacion": tasaBd
    }

    return resumen

#print(resumen_cursos(matriculas)) #Comentar/Descomentar si quiere que aparezca por consola el resultado de def resumen_cursos

def resumen_cursos_2(listaMatriculas):
    resumen2 = {}
    for lm in listaMatriculas:
        curso2 = lm['curso']
        if curso2 not in resumen2:
            resumen2[curso2] = {
                "matriculados": 0,
                "finalizados": 0,
                "suma_notas": 0.0,
                "num_notas": 0
            }
        resumen2[curso2]["matriculados"] +=1
        if lm['finalizado']:
            resumen2[curso2]["finalizados"] += 1
            resumen2[curso2]["suma_notas"] += lm['nota']
            resumen2[curso2]["num_notas"] += 1
    for curso2, datos in resumen2.items():
        notaMedia = datos["suma_notas"] / datos["num_notas"] if datos["num_notas"] > 0 else None
        datos["nota_media"] = notaMedia
        tasaFin = (datos["finalizados"] / datos["matriculados"]) * 100 if datos["matriculados"] > 0 else None
        datos["tasa_finalizacion"] = tasaFin
        del(datos["suma_notas"], datos["num_notas"])

    return resumen2

print(resumen_cursos_2(matriculas))