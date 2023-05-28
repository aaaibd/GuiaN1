n = int(input("Por favor ingrese un valor: "))

def cubo_n(n):
    for i in range(1,n+1):
        cub = i**3
        print(f"El cubo de {i} es:{cub}")
cubo_n(n)