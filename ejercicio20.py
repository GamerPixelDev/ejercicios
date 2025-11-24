partidas = [
    {"jugador": "Ana", "modo": "ranked", "kills": 10, "muertes": 2, "asistencias": 5, "duracion": 32},
    {"jugador": "Ana", "modo": "normal", "kills": 7, "muertes": 1, "asistencias": 3, "duracion": 27},
    {"jugador": "Ana", "modo": "ranked", "kills": 2, "muertes": 0, "asistencias": 10, "duracion": 20},
    {"jugador": "Luis", "modo": "normal", "kills": 3, "muertes": 5, "asistencias": 2, "duracion": 25},
    {"jugador": "Carla", "modo": "ranked", "kills": 15, "muertes": 3, "asistencias": 10, "duracion": 45},
    {"jugador": "Carla", "modo": "normal", "kills": 4, "muertes": 4, "asistencias": 6, "duracion": 30},
    {"jugador": "Jorge", "modo": "ranked", "kills": 4, "muertes": 1, "asistencias": 3, "duracion": 18},
    {"jugador": "Mara", "modo": "normal", "kills": 20, "muertes": 10, "asistencias": 5, "duracion": 40},
]

def resumen_jugador(listaPartidas, nombreJugador):
    player = [p for p in listaPartidas
                if p['jugador'] == nombreJugador
            ]
    #Devuelve un diccionario vacío si no encuentra alguna coincidencia
    if not player:
        return {}
    #Guardamos el nombre del jugador en una variable
    player1 = player[0]['jugador']
    #COntamos las partidas que ha jusdo el jugador
    totalPartidas = len(player)
    #KDA medio más alto
    kdas = []
    for p in player:
        kda_partida = (p['kills'] + p['asistencias']) / max(1, p['muertes'])
        kdas.append(kda_partida)
    totalKda = round(sum(kdas) / len(kdas), 2)
    #Guardamos en cada variable el modo de juego para luego compararlo
    totalRankeds = 0
    totalNormal = 0
    for p1 in player:
        if p1['modo'] == 'ranked':
            totalRankeds += 1
        else:
            totalNormal +=1
    if totalRankeds > totalNormal:
        modoJugado = "ranked"
    elif totalRankeds == totalNormal:
        modoJugado = "ambos por igual"
    else:
        modoJugado = "normal"
    #Averiguamos cual es la mejor partida mediate el kda medio de cada partida
    mejor = None
    mejor_kda = -1
    for p in player:
        kda = (p['kills'] + p['asistencias']) / max(1, p['muertes'])
        if kda > mejor_kda:
            mejor_kda = kda
            mejor = p
    #Montamos la variable con la mejor partida
    mejor_partida = f"{mejor['modo']} - {mejor['kills']}/{mejor['muertes']}/{mejor['asistencias']} en {mejor['duracion']}min"
    #Diccionario a devolver
    resumen = {
        "jugador": player1,
        "total_partidas": totalPartidas,
        "kda_medio": totalKda,
        "modo_mas_jugado": modoJugado,
        "mejor_partida": mejor_partida
    }
    return resumen

print(resumen_jugador(partidas, "Ana"))
print(resumen_jugador(partidas, "Carla"))
print(resumen_jugador(partidas, "Pepito"))  # debería dar {}
