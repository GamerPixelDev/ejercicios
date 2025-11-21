#Ejercicio 18 – Filtrado múltiple con vuelos
#Objetivo:
#   Devuelva únicamente vuelos que sean directos.
#   Sean más baratos de 150€.
#   Y tengan una duración inferior a 180 minutos.
#La función debe devolver una lista así:
#   ["IB123 – 180€ – 150min", "AF980 – 150€ – 130min"] Pero solo con los vuelos que cumplan las condiciones.

vuelos = [
    {"codigo": "IB123", "origen": "Madrid", "destino": "Roma", "duracion": 150, "precio": 180, "directo": True},
    {"codigo": "LH450", "origen": "Barcelona", "destino": "Berlin", "duracion": 240, "precio": 220, "directo": False},
    {"codigo": "AF980", "origen": "Madrid", "destino": "París", "duracion": 130, "precio": 150, "directo": True},
    {"codigo": "RY300", "origen": "Sevilla", "destino": "Londres", "duracion": 170, "precio": 90, "directo": True},
    {"codigo": "VY777", "origen": "Madrid", "destino": "Dublín", "duracion": 200, "precio": 110, "directo": False},
    {"codigo": "UX555", "origen": "Valencia", "destino": "Roma", "duracion": 145, "precio": 160, "directo": True},
]

def vuelos_baratos_rapidos(listaVuelos):
    baratos = [b for b in listaVuelos
                if b["directo"]
                and b["precio"] < 150
                and b["duracion"] < 180
            ]
    return [f"{r['codigo']} - {r['precio']}€ - {r['duracion']}min" for r in baratos]

print(vuelos_baratos_rapidos(vuelos))
