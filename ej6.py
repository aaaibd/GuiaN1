#Reloj que comienza desde las 00:00:00 hasta las 23:59:59
for hora in range (0,24):
    for minutos in range (0,60):
        for segundos in range (0,60):
            print("La Hora es: ", f"{hora:02d}:{minutos:02d}:{segundos:02d}")
