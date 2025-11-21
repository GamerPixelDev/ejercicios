#Ejercicio 17 — “Viajes internacionales y alertas”
#Tienes una lista de viajes. Cada viaje contiene:
#   pasajero
#   pais_destino
#   dias_estancia
#   precio_total
#   requiere_visa (True/False)
#Tu misión:
#Crear una función viajes_alerta(listaViajes) que devuelva solo los viajes que cumplen estas condiciones simultáneamente:
#   El destino requiere visado.
#   La estancia es mayor de 7 días.
#   El precio total es superior a 1200€.
#La función debe devolverlos ordenados de mayor a menor precio y en formato:
#   "Pasajero — País — Precio€"

viajes = [
    {"pasajero": "Ana Torres", "pais_destino": "Japón", "dias_estancia": 10, "precio_total": 2400, "requiere_visa": True},
    {"pasajero": "Luis Pérez", "pais_destino": "Canadá", "dias_estancia": 5, "precio_total": 1500, "requiere_visa": True},
    {"pasajero": "Clara Gómez", "pais_destino": "Portugal", "dias_estancia": 8, "precio_total": 900, "requiere_visa": False},
    {"pasajero": "Jorge Ruiz", "pais_destino": "Estados Unidos", "dias_estancia": 12, "precio_total": 1800, "requiere_visa": True},
    {"pasajero": "Mara Rivera", "pais_destino": "Reino Unido", "dias_estancia": 9, "precio_total": 1100, "requiere_visa": False},
    {"pasajero": "Daniel Soto", "pais_destino": "Australia", "dias_estancia": 14, "precio_total": 3200, "requiere_visa": True}
]

def viajes_alerta(listaViajes):
    viajesPro = [vp for vp in listaViajes
                    if vp["requiere_visa"]
                    and vp["dias_estancia"] > 7
                    and vp["precio_total"] > 1200
                ]
    viajesPro.sort(key=lambda v: -v["precio_total"])
    return [f"{r['pasajero']} - {r['pais_destino']} - {r['precio_total']}€" for r in viajesPro]

print(viajes_alerta(viajes))