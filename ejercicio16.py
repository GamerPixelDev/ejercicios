#Ejercicio 16 — Reservas de hotel sospechosas
#Tienes una lista de reservas de hotel. Cada reserva tiene:
#   "cliente" → nombre del cliente
#   "noches" → número de noches que quiere quedarse
#   "precio_noche" → precio por noche
#   "destino" → ciudad del hotel
#   "cancelada" → si la reserva fue cancelada o no
#Una reserva será considerada "sospechosa" si:
#   El importe total supera 900 €,
#   Y NO está cancelada,
#   Y el destino empieza por la letra "M" (Madrid, Málaga, Marsella…).
#Tu función debe devolver una lista con cadenas tipo:
#   "Cliente — Destino — ImporteTotal€"
#ordenadas de mayor a menor importe total.

reservas = [
    {"cliente": "Ana Torres", "noches": 3, "precio_noche": 150, "destino": "Madrid", "cancelada": False},
    {"cliente": "Luis Pérez", "noches": 2, "precio_noche": 120, "destino": "Barcelona", "cancelada": False},
    {"cliente": "Clara Gómez", "noches": 5, "precio_noche": 90, "destino": "Málaga", "cancelada": False},
    {"cliente": "Jorge Ruiz", "noches": 7, "precio_noche": 80, "destino": "Valencia", "cancelada": False},
    {"cliente": "Mara Rivera", "noches": 4, "precio_noche": 250, "destino": "Marsella", "cancelada": True},
    {"cliente": "Daniel Soto", "noches": 6, "precio_noche": 200, "destino": "Mallorca", "cancelada": False}
]

def reservas_sospechosas(listaReservas):
    sospechosas = [s for s in listaReservas
                    if (s["precio_noche"] * s["noches"]) > 900
                    and not s["cancelada"]
                    and s["destino"][0].upper() == "M"
                ]
    sospechosas.sort(key=lambda s: -s["precio_noche"] * s["noches"])
    return [f"{r['cliente']} - {r['destino']} - {r['precio_noche'] * r['noches']}€" for r in sospechosas]

print(reservas_sospechosas(reservas))