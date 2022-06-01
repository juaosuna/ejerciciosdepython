# hacer un programa que pida un caracter e indique si es una vocal o no

letra= input("digite un caracter:").lower()

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print("es una vocal")

else: 
    print("No es una vocal")