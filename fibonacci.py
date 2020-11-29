# imprimir  la sequencia de fibonacci hasta el rango correspondiente
# 0, 1, 1, 2, 3, 5, 8, 13 ....

try:
    numero = int(input('Introdusca el rango para obtener la secuencia de fibonacci: '))
except ValueError:
    print("VALOR InVALIDO, por favor introdusca un numero entero positivo")
else:
    if numero <= 0:
        print("VALOR INVALIDO, por favor introdusca un numero entero positivo")
    else:
        i = 0
        n1 = 0
        n2 = 1
        list =[""]
        while i < numero:
            print(n1, end=",")
            nn = n1 + n2
            n1 = n2
            n2 = nn
            i += 1


