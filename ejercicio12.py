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