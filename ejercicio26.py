#Ejercicio 26 - Sistemas de soporte técnico
#A) resumen_soporte(listaTickets)
#    Devuelve un diccionario con:
#        "total_tickets" → número total.
#        "resueltos" → cuántos tienen resuelto == True.
#        "pendientes" → cuántos tienen resuelto == False.
#        "porcentaje_resueltos" → porcentaje (0–100, con decimales) respecto al total.
#        "tiempo_medio_resolucion" → media de tiempo_resolucion solo de tickets resueltos (ignora None). Si no hay ninguno resuelto, pon None.
#        "top_agente" → nombre del agente que más tickets resueltos tiene (si hay empate, cualquiera de los top vale).
#B) ranking_categorias(listaTickets)
#    Devuelve una lista de strings con este formato:
#        "correo -> 3 tickets (1 pendientes)"
#        "impresora -> 3 tickets (2 pendientes)"
#        ...
#    Para cada categoría:
#        Cuenta cuántos tickets totales tiene.
#        Cuenta cuántos están pendientes.
#        Ordena la lista:
#        Primero por tickets totales (de mayor a menor).
#        Si empatan, por pendientes (de mayor a menor).
#        Si aún empatan, por nombre de categoría alfabético ascendente (para que sea determinista).
#C) alertas_criticas(listaTickets)
#    Queremos una lista de tickets peligrosos:
#        Un ticket es “crítico” si:
#        resuelto == False, y además
#        o bien prioridad es "alta" o "critica",
#        o bien horas_abierto > 72.
#    Devuelve una lista de strings, ordenada de más urgente a menos, con este formato:
#        "[CRÍTICO] ID 3 — prioridad critico — 80h abierto"
#        "[CRÍTICO] ID 10 — prioridad critico — 120h abierto"
#        ...
#    Orden:
#        Primero los de prioridad "critica".
#        Luego "alta".
#        Dentro de cada grupo, ordena por horas_abierto de mayor a menor.
#    Pista para el orden: puedes usar un sorted con un key que use una tupla, por ejemplo convirtiendo la prioridad a un número (critica=2, alta=1, resto=0) y luego las horas.

tickets = [
    {"id": 1, "usuario": "Ana",   "categoria": "correo",      "prioridad": "alta",    "resuelto": True,  "horas_abierto": 5,   "agente": "Laura",  "tiempo_resolucion": 4},
    {"id": 2, "usuario": "Luis",  "categoria": "impresora",   "prioridad": "media",   "resuelto": False, "horas_abierto": 30,  "agente": "Carlos", "tiempo_resolucion": None},
    {"id": 3, "usuario": "Ana",   "categoria": "red",         "prioridad": "critica", "resuelto": False, "horas_abierto": 80,  "agente": "Laura",  "tiempo_resolucion": None},
    {"id": 4, "usuario": "Clara", "categoria": "correo",      "prioridad": "baja",    "resuelto": True,  "horas_abierto": 10,  "agente": "Marta",  "tiempo_resolucion": 9},
    {"id": 5, "usuario": "Jorge", "categoria": "impresora",   "prioridad": "alta",    "resuelto": True,  "horas_abierto": 50,  "agente": "Carlos", "tiempo_resolucion": 40},
    {"id": 6, "usuario": "Mara",  "categoria": "aplicacion",  "prioridad": "media",   "resuelto": False, "horas_abierto": 10,  "agente": "Laura",  "tiempo_resolucion": None},
    {"id": 7, "usuario": "Luis",  "categoria": "aplicacion",  "prioridad": "critica", "resuelto": True,  "horas_abierto": 100, "agente": "Marta",  "tiempo_resolucion": 90},
    {"id": 8, "usuario": "Ana",   "categoria": "impresora",   "prioridad": "alta",    "resuelto": False, "horas_abierto": 73,  "agente": "Carlos", "tiempo_resolucion": None},
    {"id": 9, "usuario": "Clara", "categoria": "red",         "prioridad": "media",   "resuelto": True,  "horas_abierto": 20,  "agente": "Laura",  "tiempo_resolucion": 18},
    {"id": 10,"usuario": "Mara",  "categoria": "correo",      "prioridad": "critica", "resuelto": False, "horas_abierto": 120, "agente": "Marta",  "tiempo_resolucion": None},
]

def resumen_soporte(listaTickets):
    resumen = {}
    agentes = {}
    total = 0
    resueltos = 0
    pendientes = 0
    tiempo = 0
    for id in listaTickets:
        total += 1
        if id["resuelto"]:
            resueltos += 1
        else:
            pendientes +=1
        if id["tiempo_resolucion"] is not None:
            tiempo += id["tiempo_resolucion"]
        agente = id["agente"]
        if agente not in agentes:
            agentes[agente] = 0
        if id["tiempo_resolucion"] is not None and id["resuelto"]:
            agentes[agente] += 1
    porcentajeResueltos = round((resueltos / total) * 100, 1)
    tiempoMedio = round(tiempo / total, 1)
    top_agente = max(agentes)
    resumen = {
        "total_tickets": total,
        "resueltos": resueltos,
        "pendientes": pendientes,
        "porcentaje_resueltos": porcentajeResueltos,
        "tiempo_medio_resolucion": tiempoMedio,
        "top_agente": top_agente
    }
    return resumen

print(resumen_soporte(tickets))