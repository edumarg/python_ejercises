# Encontrar el factorial de un numero
try:
    numero = int(input('Introdusca un numero para encntrar su factorial: '))
except ValueError:
    print('VALOR NO VALIDO, por favor introdusca un numero entero:')
else:
    if numero < 0:
        print("'VALOR NO VALIDO, los numeros negativos no tienen factorial")
    else:
        rango = range(1,numero + 1)
        factorial = 1
        for r in rango:
            factorial *= r
        print(f'El factorial de {numero}  es {factorial}')
