#Ejercicio 12 — “Paquetes por enviar”
#Crea una función llamada envios_prioritarios que:
#    Se quede solo con los envíos que:
#        vayan a Madrid,
#        y tengan peso mayor de 2 kg,
#        o sean urgentes (aunque no vayan a Madrid).
#    Ordene esos envíos por peso de mayor a menor.
#    Devuelva una lista de strings con el formato:
#        "ID 105 → 3.3kg (Urgente)"
#        "ID 101 → 2.5kg (Urgente)"
#        "ID 103 → 1.1kg"
#        etc.
#Nota: solo añade “(Urgente)” si el envío lo es.

envios = [
    {"id": 101, "peso": 2.5, "destino": "Madrid", "urgente": True},
    {"id": 102, "peso": 7.2, "destino": "Valencia", "urgente": False},
    {"id": 103, "peso": 1.1, "destino": "Madrid", "urgente": False},
    {"id": 104, "peso": 12.0, "destino": "Sevilla", "urgente": True},
    {"id": 105, "peso": 3.3, "destino": "Madrid", "urgente": True},
]

def envios_prioritarios(listaEnvios):
    enviosUrgentes = [eu for eu in listaEnvios if (eu["destino"] == "Madrid" and eu["peso"] > 2) or eu["urgente"]]
    ordenados = sorted(enviosUrgentes, key=lambda o: o["peso"], reverse=True)
    return [f"ID {r['id']} -> {r['peso']}kg {'(Urgente)' if r['urgente'] else ''}" for r in ordenados]

print(envios_prioritarios(envios))

#Ejercicio 12B — “La clasificación imposible… hasta que la ves”
#Partimos de la misma lista de envíos, pero ahora la función se llama envios_clasificados y cambia el juego.
#Nuevas reglas infernales:
#   Filtra los envíos según estas normas:
#       Entran todos los urgentes.
#       Entran los que vayan a Madrid si pesan más de 1.5 kg.
#       Entran los que pesen más de 10 kg vaya donde vayan, aunque no sean urgentes.
#   Una vez filtrados, ordénalos así:
#       Primero los urgentes, ordenados por peso descendente.
#       Después los no urgentes, también por peso descendente.
#   Y aquí viene la salsa:
#       Devuelve una lista de strings con este formato:
#           [URGENTE] ID 104 → 12.0kg → Sevilla
#           [NORMAL]  ID 105 → 3.3kg → Madrid
#       El prefijo va entre corchetes.
#       El destino debe ir siempre al final.
#   Para rematar:
#       Si el envío pesa más de 8kg, añade al final: "⚠️ PESADO" (sin paréntesis, a pelo)

def envios_clasificados(listaEnvios):
    enviosUrgentes = [eu for eu in listaEnvios
                        if eu["urgente"]
                            or (eu["destino"] == "Madrid" and eu["peso"] > 1.5)
                            or eu["peso"] > 10
                    ]
    ordenados = sorted (enviosUrgentes, key=lambda o: (o["urgente"] and o["peso"], not o["urgente"] and o["peso"]), reverse=True)
    return [f"{'[URGENTE]' if r['urgente'] else '[NORMAL]'} ID {r['id']} -> {r['peso']}kg -> {r['destino']} {'⚠️ PESADO' if r['peso'] > 8 else ''}" for r in ordenados]

print(envios_clasificados(envios))