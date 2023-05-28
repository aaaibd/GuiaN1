listadenumeros=[40+(i*15) for i in range(20)]
print("La lista generada es: ", listadenumeros)

numeroparabuscar= int(input("Segun la lista ingrese un numero: "))
repeticion= 0
for listadenumeros in listadenumeros:
    if listadenumeros==numeroparabuscar:
        repeticion +=1
print("Este numero se repite: ", numeroparabuscar, " veces en la lista", repeticion)
