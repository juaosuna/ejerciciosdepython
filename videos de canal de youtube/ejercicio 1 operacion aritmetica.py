#Escribir la siguiente expresion en forma de expresion algoritmica
#a*3x(b*2-2ac) sobre 2b

a = float(input("a->"))
b = float(input("b->"))
c = float(input("c->"))
resultado = (a**3 * (b**2 - 2*a*c))/(2*b)
print(f"El resultado es :{resultado}")