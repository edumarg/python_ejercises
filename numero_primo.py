# revisar si un numero es primo
try:
    numero = int(input('Ingrese numero para comprova si es primo: '))
except ValueError:
    print("Valor no valido, por favor ingrese un valore correcto")
else:
    if numero < 1:
        print(' los numeros primos son mayores a 0')
    if numero == 1:
        print('1 es un numero PRIMO')
    if numero > 1:
        for r in range(2, numero):
            if numero % r == 0:
                print(f'{numero}  NO es un numero PRIMO')
                break
        else:
            print(f'{numero} es un numero PRIMO')

# revisar numeros primos en un rango

try:
    rango = int(input('Ingrese rango para comprova si es primo: '))
except ValueError:
    print("Valor no valido, por favor ingrese un valor numero entero posiivo")
else:
    for numero in range(rango + 1):
        if numero > 1:
            for i in range(2, numero):
                if numero % i == 0:
                    print(f'{numero}  NO es un numero PRIMO')
                    break
            else:
                print(f'{numero} es un numero PRIMO')

