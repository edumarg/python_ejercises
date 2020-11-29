# convertir Km to millas y millas a Km
print('-Conversor Km a M y M a Km')
try:
    valor_original = float(input('Distancia a convertir sin unidad: '))
except ValueError:
    print('Valor de distancia invalido, por favor ingrese una distancia valida')
else:
    unidad_original = input('Medida a convertir: [K]m a Millas o [M]illas a Km: ').lower()
    if float(valor_original) >= 0:
        if unidad_original == 'k':
            valor_converido = valor_original * 0.621371
            print(f' {valor_original} Km equivalen a {valor_converido} millas ')
        elif unidad_original == 'm':
            valor_converido = valor_original / 0.621371
            print(f' {valor_original} millas equivalen a {valor_converido} Km ')
        else:
            print('Unidad no valida, por valor ingrese una unidad valida [K]m o [M}illas')
