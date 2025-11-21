#Ejercicio 14 – “Becas universitarias”
#Tienes una lista de diccionarios con solicitudes de becas. Cada solicitud tiene:
#    "nombre" (str)
#    "nota_media" (float)
#    "ingresos_familia" (int, en euros)
#    "voluntariado" (bool)
#    "modalidad" (str → "general" o "excelencia")
#Reglas para seleccionar a los becados:
#    Beca general:
#        Ingresos familiares < 20 000
#        Nota media ≥ 6
#        Si hace voluntariado, va antes en la lista final.
#    Beca excelencia:
#        Nota media ≥ 9
#        Da igual ingresos y voluntariado.
#La función debe:
#    Filtrar los que cumplen su modalidad correspondiente.
#    Ordenarlos así:
#        Primero los de excelencia, ordenados por nota de mayor a menor.
#        Después los de general, ordenados así:
#            Voluntariado primero.
#            Dentro de cada grupo, ordenar por nota de mayor a menor.
#Debe devolver una lista de strings tipo:
#    "Ana — excelencia — 9.5"
#    "Luis — general — 7.2 (voluntario)"
#    "Carla — general — 6.3"

solicitudes = [
    {"nombre": "Carlos Gallego", "nota_media": 7.8, "ingresos_familia": 40000, "voluntariado": True, "modalidad": "general"},
    {"nombre": "Ana Ruiz", "nota_media": 9.4, "ingresos_familia": 52000, "voluntariado": False, "modalidad": "excelencia"},
    {"nombre": "Luis Martín", "nota_media": 6.5, "ingresos_familia": 15000, "voluntariado": True, "modalidad": "general"},
    {"nombre": "María López", "nota_media": 8.3, "ingresos_familia": 18000, "voluntariado": False, "modalidad": "general"},
    {"nombre": "Claudia Vega", "nota_media": 9.1, "ingresos_familia": 9000, "voluntariado": True, "modalidad": "excelencia"}
]

def selecion_becas(listaSolicitudes):
    becasGeneral = [bg for bg in listaSolicitudes
                        if bg["modalidad"] == "general" and bg["ingresos_familia"] < 20000 and bg["nota_media"] >= 6
                    ]
    becasExcelencia = [be for be in listaSolicitudes
                        if be["modalidad"] == "excelencia" and be["nota_media"] >= 9
                    ]
    ordenadosGenerales = sorted(becasGeneral, key=lambda og: (-og["voluntariado"], -og["nota_media"]))
    ordenadosExcelentes = sorted(becasExcelencia, key=lambda oe: -oe["nota_media"])
    return [f"{re['nombre']} — {re['modalidad']} — {re['nota_media']} {'(voluntario)' if re['voluntariado'] else ''}" for re in ordenadosExcelentes] + [f"{ro['nombre']} — {ro['modalidad']} — {ro['nota_media']} {'(voluntario)' if ro['voluntariado'] else ''}" for ro in ordenadosGenerales]

print(selecion_becas(solicitudes))