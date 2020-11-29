# revisar si un texto es palindromo -se lee igual al derecho que al reves

texto = list(input('ingrese una frace para determinar si es un palindromo: ').lower())
repeticiones = texto.count(" ")
print(repeticiones)
i = 1
while i <= repeticiones:
    texto.remove(' ')
    i += 1
reverse_text = texto.copy()
reverse_text.reverse()
print(texto)
print(reverse_text)
if texto == reverse_text:
    print('la frase es un palindromo')
else:
    print('la frase NO es un palindromo')


