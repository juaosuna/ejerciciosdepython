#que muestre de 20 numeros y dentro de esos 20 numeros va mostrar su potencia
print("calcular las potencias de 20 numeros")
base=int(input("digite la base: "))
exponente=base
def generar_potencias(base,exponente):
    base=int(input("digite la base: "))
    resultado=1 
    for i in range(exponente):
        resultado *= base
    return resultado

print(generar_potencias(base,exponente))