# Suma de dos numeros
print('---suma de dos  numeros---')
n1 = float(input('primer numero a sumar:'))
n2 = float(input('segundo numero a sumar:'))
result = n1 + n2
print(result)

# raiz cuadrada
print('---raiz cuadrada')
num = int(input('Numero al cual se le quire obtener la raiz cuadrada: '))
raiz = num ** 0.5
print(raiz)

# Ec. Cuadradicas ax**2 + bx + c = 0
# Sol = (-b + sqr(b**2 - 4*a*c))/(2*a) y (-b - sqr(b**2 - 4*a*c))/(2*a)
print('---Ec. Cuadradicas ax**2 + bx + c = 0---')
a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

d = (b ** 2 - 4 * a * c) ** 0.5
sol1 = (-b + d) / (2 * a)
sol2 = (-b - d) / (2 * a)

print(f'The solutions for the Ec. {a}x**2 + {b}x + {c} are: Sol1 {sol1} and Sol2 {sol2}')

# Swapp variables
print('---Swapp variables')
x = input('primera variable: ')
y = input('segunda variable: ')
x, y = y, x
print(f'Las variables despues de intercambiarlas quedan como "x" = {x} y "y" = {y}')



