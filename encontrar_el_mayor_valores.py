# Encontrar el mayor de los valores
valores = input('ingrese varios valores separados por espacio, para determinar cual es el mayor : ')
lista = valores.split()
v_max = 0
for v in lista:
    if int(v) > v_max:
        v_max = int(v)
print(v_max)
