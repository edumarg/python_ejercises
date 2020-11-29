# la computadora pienza en un numero del 1 al 100 y el usuario debe divinarlo

import random

print(' Estoy pensando un numero del 1 al 100, trata de adivinarlo en la menor cantidad de intentos posibles')
numero = random.randint(1, 100)
intentos = 0
while True:
    intentos += 1
    try:
        answer = int(input(">> "))
    except ValueError:
        print('Por favor ingresa un valor valido. Numero entero del 1 al 100')
    else:
        if not 100 > answer > 0:
            print('Por favor ingresa un valor valido. Numero entero del 1 al 100')
        elif answer == numero:
            print(f'Adivinaste. {numero} es el numero que pense y te tomo solo {intentos} intentos adivinarlo')
            break
        elif answer != numero:
            if answer > numero:
                print(
                    f'Lo siento, {answer} no es el numero que estoy pensando. El numero que estoy pensando es menor a {answer}.'
                    f'Sigue intentando')
            elif answer < numero:
                print(
                    f'Lo siento, {answer} no es el numero que estoy pensando. El numero que estoy pensando es mayor a {answer}.'
                    f'Sigue intentando')
