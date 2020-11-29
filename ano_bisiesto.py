# determinar a~o bisiestro
# Cómo saber si un año va a ser bisiesto
# 	1- Los años bisiestos son los divisibles entre 4 (como 2004, 2008, etc.)
#  	2- excepto si es divisible entre 100, entonces no es bisiesto (como 2100, 2200, etc.)
#  	3- excepto si es divisible entre 400, entonces sí (como 2000, 2400)

try:
    year = int(input('Elija un a~o para determinar si es BISIESTRO: '))
except ValueError:
    print('Valor no valido, por favor introdusca un valor de a~o valido -solo numeros- YYYY')
else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'El a~o {year} es un a~o BISIESTRO')
            else:
                print(f'El a~o {year} NO es un a~o BISIESTRO')
        else:
            print(f'El a~o {year} es un a~o BISIESTRO')
    else: print(f'El a~o {year} NO es un a~o BISIESTRO')