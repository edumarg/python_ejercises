# determinar si un unmero es par o impar
try:
    numero = float(input('ingrese un numero: '))
except ValueError:
    print('Valor no valido, por favor ingrese un numero valido')
else:
    if numero == 0:
        print(f'{numero} es ZERO')
    elif numero % 2 == 0:
        print(f'{numero} es un numero PAR')
    else:
        print(f'{numero} es un numero IMPAR')

# determinar los numeros pares e impares dentro de un rango
try:
    rango = int(input('ingrese el valor de rango: '))
except ValueError:
    print('Valor no valido, por favor ingrese un rango valido: ')
else:
    for r in range(rango+1):
        if r % 2 == 0:
            print(f'El numero {r} es PAR')
        else:
            print(f'El numero {r} es IMPAR')