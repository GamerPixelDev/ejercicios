#Ejercicio 19 – Partidas “TOP” en modo competitivo
#Define una función partidas_destacadas(listaPartidas) que:
#   Considere solo las partidas en modo "ranked".
#   Calcule el KDA de cada partida como:
#       𝐾𝐷𝐴=kills+asistencias / max(1,muertes)
#   Se quede solo con las partidas que cumplan:
#       KDA >= 3
#   duracion >= 20 minutos
#   Devuelva una lista de cadenas, ordenada:
#       Primero, de mayor KDA a menor
#       En caso de empate de KDA, de menor a mayor duración
#       Cada cadena tendrá este formato exacto:
#           NOMBRE - KDA X.XX - Ymin (ranked)
#   Ejemplo (formato, no datos reales):
#       "Ana - KDA 3.50 - 32min (ranked)"

partidas = [
    {"jugador": "Ana", "modo": "ranked", "kills": 10, "muertes": 2, "asistencias": 5, "duracion": 32},
    {"jugador": "Luis", "modo": "normal", "kills": 3, "muertes": 5, "asistencias": 2, "duracion": 25},
    {"jugador": "Carla", "modo": "ranked", "kills": 15, "muertes": 3, "asistencias": 10, "duracion": 45},
    {"jugador": "Jorge", "modo": "ranked", "kills": 4, "muertes": 1, "asistencias": 3, "duracion": 18},
    {"jugador": "Mara", "modo": "normal", "kills": 20, "muertes": 10, "asistencias": 5, "duracion": 40},
    {"jugador": "Sergio", "modo": "ranked", "kills": 8, "muertes": 4, "asistencias": 12, "duracion": 28},
]

def partidas_destacadas(listaPartidas):
    partidas = [p for p in listaPartidas
                    if p['modo'] == "ranked"
                    and ((p['kills'] + p['asistencias']) / max(1, p['muertes'])) >= 3
                    and p['duracion'] >= 20
                ]
    partidas.sort(key=lambda po: (-(po['kills'] + po['asistencias']) / max(1, po['muertes']), po['duracion']))
    return [f"{r['jugador']} - KDA {(r['kills'] + r['asistencias']) / max(1, r['muertes'])} - {r['duracion']}min {'(ranked)' if r['modo'] == 'ranked' else ''}" for r in partidas]

print(partidas_destacadas(partidas))

def partidas_destacadas_2(listaPartidas):
    partidas_filtradas = [
        p for p in listaPartidas
        if p['modo'] == "ranked"
        and (p['kills'] + p['asistencias']) / max(1, p['muertes']) >= 3
        and p['duracion'] >= 20
    ]
    partidas_filtradas.sort(
        key=lambda po: (
            -((po['kills'] + po['asistencias']) / max(1, po['muertes'])),
            po['duracion']
        )
    )
    resultado = []
    for r in partidas_filtradas:
        kda = (r['kills'] + r['asistencias']) / max(1, r['muertes'])
        resultado.append(
            f"{r['jugador']} - KDA {kda:.2f} - {r['duracion']}min (ranked)"
        )
    return resultado

print(partidas_destacadas_2(partidas))