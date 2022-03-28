ruta = '//1.1.1.1/eoi/python'

ruta = ruta[2:]
barra = ruta.index('/')

eguipo = ruta[:barra]
ruta = ruta[barra:]
print(f'eguipo={eguipo}; ruta={ruta}')
