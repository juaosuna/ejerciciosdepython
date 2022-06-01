#ejemplo1 

import math

numero= int(input("digite un numero:"))
while numero<0:
    print("Error, deberia ser un numero positivo")
    numero= int(input("digite un numero:"))
print(f"\nsu raiz cuadrada es: {(math.sqrt(numero)):.2f}")


#ejemplo 2
i= 1
while i<=10:
    print(i)
    i += 1