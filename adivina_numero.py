# adivinar el numero de 1 a 10
import random
numero_adivinar = random.randint(1, 10)

try:
    numero_usuario = int(input('Adivine el numero del 1 al 10: '))
except ValueError:
    print('ingreso un valor no valido, por favor introdusca un numero entero del 1 al 10')
else:
    if numero_usuario > 10:
        print(
            'ingreso un valor no valido, or favor introdusca un numero entero del 1 al 10')
    elif numero_usuario < 0:
        print(
            'ingreso un valor no valido, or favor introdusca un numero entero del 1 al 10')
    elif numero_adivinar == numero_usuario:
        print(' Ganaste, ese era el numero!!!')
    elif numero_usuario > numero_adivinar:
        print('el numero que elegiste esta por encima del numero secreto!!')
    elif numero_adivinar > numero_usuario:
        print('el numero que elegiste esta por debajo del numero secreto!')
print(f'el numero secreto es {numero_adivinar}')
