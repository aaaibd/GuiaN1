n = int(input("Ingrese un número: "))
factorial = 1

for i in range(1,n+1):
    factorial*=i
if factorial == 0:
    print(1)
print (f"El fatorial del número {n}! es: {factorial}")