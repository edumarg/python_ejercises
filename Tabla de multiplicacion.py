# Mostrar la tabla de multiplicacion de un numero determinado
try:
    numero = int(input('Introdusca un numero entero y para mostrar su tabla de multiplicacion -Del 1 al 10-: '))
except ValueError:
    print('El valor introducido no es valido, por favor ingrese un valor valido)')
else:
    rango = range(11)
    for r in rango:
        print(f'{r} x {numero} = {r * numero}' )