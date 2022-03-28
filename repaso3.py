TABLA_DE_CONTROL = 'TRWAGMYFPDXBNUZSQVHLCKE'

nif = '12345678'
control_digital = TABLA_DE_CONTROL[int(nif) % 23]
whole_nif = nif + control_digital

print(whole_nif)
