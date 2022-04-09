print("ingresar el numero inicial")
i = int(input("ingrese el numero inicial: "))
print("ingrese el numero final")
f = int(input("ingrese el numero final: "))
suma = 0
print("**los numeros pares del rango**")
while i <= f:
    if i % 2 == 0:
        print(i)
    i+=1
    suma=suma+1
print("la suma de los numeros es:", suma)
