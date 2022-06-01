# construir un programa que simule el funcionamiento de una calculadora que puede realizar
#las cuatro operaciones aritmeticas basicas(su,a,resta,multiplicacion y division).
#el usuario debe especificar la operacion con el primer caracter del nombre de la operacion.

# S , s - Suma
# R , r -Resta
# P , p , M, m -Multiplicacion
# D , d - Division
# RD, rd - residuo de la division
#upper _ es para convertir las letras en mayuscula 

from ast import Break

num1 = float(input("Digite un numero:"))
num2 = float(input("Digite un numero:"))
operacion = input("digite la operacion:").upper()
Opcionoperacion=int(input("digite tipo de salida 4.Resultado 5.salir:"))


while Opcionoperacion:
    if operacion== 'S':
       suma = num1+num2
    print(f"\n la suma es:{suma}")
    
    if operacion== 'R':
     resta = num1-num2
    print(f"\n la resta es:{resta}")
     
     
    if operacion== 'M' or operacion=='p':
     mult = num1*num2
    print(f"\n la multiplicacion es:{mult}")


    if operacion== 'D':
     div= num1/num2
    print(f"\n la division es:{div:.2f}")


    if operacion=='J':
     resi= num1%num2
    print(f"\n el residuo de la division es:{resi:.2f}")
     
print("Gracias por utilizar la calculadora")
    

 
