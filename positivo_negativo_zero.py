# Chequear si un numero es positivo, negativo o zero
try:
    numero = float(input('ingrese un numero: '))
except ValueError:
    print('Valor no valido, por favor ingrese un numero valido')
else:
    if numero > 0:
        print(f'{numero} es un numero positivo')
    elif numero < 0:
        print(f'{numero} es un numero negativo')
    else:
        print(f'{numero} es ZERO')