def celsius(f):
    return (f - 32) * 5 / 9


def farenheit(c):
    return c * (9 / 5) + 32


print('---Convertir unidades de temperatura')
unidad_original = (input('unidad a convertir: [C] a F o [F] a C: ')).lower()
if unidad_original == 'f' or unidad_original == 'c':
    try:
        temperatura_original = float(input('Temperatura a convertir:'))
    except ValueError:
        print("Valor de peso no valido, por favor inserte un valor valido")
    else:
        if unidad_original == 'f':
           temperatura_convertida = celsius((temperatura_original))
           print(f'{temperatura_original} F son equivalentes a {temperatura_convertida} C')
        elif unidad_original == 'c':
            temperatura_convertida = farenheit((temperatura_original))
            print(f'{temperatura_original} C son equivalentes a {temperatura_convertida} F')
else:
    print("unidad no valida, por favor inserte una unidad correcta")