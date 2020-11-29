# Los factores de un número son los términos en que se puede descomponer multiplicativamente el número.
# Ejemplo: Los factores de 27 son: 1 y 27 ó 3 y 9 ó 3, 3 y 3, porque: Los divisores de un número son aquellos
# números que lo dividen en forma exacta.

# encontrar los factores de un numero

try:
    numero = int(input("Ingrese un numero entero para encontrar sus factores: "))
except ValueError:
    print('Entrada invalida, por favor ingresar un numero positivo enero')
else:
    if numero < 0:
        print('Entrada invalida, por favor ingresar un numero positivo enero')
    else:
        print(f'Los factores de {numero} son:')
        for i in range (1,numero+1):
            if numero % i == 0:
                print(i)


