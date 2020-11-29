# Python Program to Find the Sum of Natural Numbers
try:
    numero = int(input("Introdusca un numero para sacar la suma de todos los numeros que lo anteceden: "))
except ValueError:
    print('Valor no valido, Introdusca in numero entero')
else:
    suma = 0
    while numero > 0:
        suma+=numero
        numero-=1
    print(suma)
