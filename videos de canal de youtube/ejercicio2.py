'''
    El tipado dinamico es que una misma variable puede
    contener diferentes tipos de datos a lo largo del programa
'''

a = input("a->")
b = input("b->")

a,b = b,a

print(f"el nuevo valor de a ess: {a}")
print(f"el nuevo valor de b ess: {b}")
