# Crear una funcion llammada fizz_buzz que cumpla con lo siguiente
# 1- Si la entrada de la funcion es divisible entre 3, la funcion debe retronar "Fizz"
# 2- Si la entrada de la funcion es divisible entre 5, funcion debe retronar "Buzz"
# 3- Si la entrada es divisible entre 3 y 5, la funcion debe retornar "FizzBuzz"
# 4- Si la entrada no es divisible ni entre 3 ni entre 5, retornar la entrada


def fizz_buzz(x):
    if (x % 3 == 0) and (x % 5 == 0):
        message = 'FizzBuzz'
    elif x % 3 == 0:
        message = 'Fizz'
    elif x % 5 == 0:
        message = 'Buzz'
    else:
        message = x
    return message


try:
    entrada = (int(input('Ingrese un numero: ')))
except ValueError:
    print('valor no valido, por favor ingrese un numero entero')
else:
    print(fizz_buzz(entrada))
