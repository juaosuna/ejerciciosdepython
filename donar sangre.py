print("Vamos a determnar si es apto para donar o no")
print("por favor llene los datos a continuacion")
edad= int(input("coloque su edad en numero entero"))
peso= int(input("coloque su peso en numero entero"))
pulso= int(input("coloque su pulso aqui entero "))
plaquetas= int(input("coloque su nivel de plaquetas"))
edadpermitida = 18 
edadpermitida2= 65
pesopermitido= 5
pulsopermitido=50
pulsopermitidomaximo=110
plaquetaspermitidad= 150000

if  edad >= edadpermitida or edad <= edadpermitida2:
    if peso > pesopermitido:
        print("es apto para donar")
    else:                
            print("no es apto para donar sangre")
                 
    if pulso >= pulsopermitido or pulso <= pulsopermitidomaximo:
        print("es apto para donar")
    else:                
        print("no es apto para donar sangre")
    if plaquetas > plaquetaspermitidad:
        print("es apto para donar sangre")
    else:                
        print("no es apto para donar sangre")       
        

 
