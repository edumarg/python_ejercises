# Find the most repeated character in a sentence
oracion = "This is a common interview question"

letra_repetida = {}
for letra in oracion:
    if letra not in letra_repetida:
        letra_repetida[letra] = 1
    else:
        letra_repetida[letra] += 1

print(letra_repetida)

letra_repetida_ordenada = sorted(letra_repetida.items(), key=lambda letras: letras[1], reverse=True)
print(letra_repetida_ordenada)
if letra_repetida_ordenada[0][1] == letra_repetida_ordenada[1][1]:
    print(
        f'Los caracteres mas repetidos son "{letra_repetida_ordenada[0][0]}" y '
        f'"{letra_repetida_ordenada[1][0]}" que se repiten {letra_repetida_ordenada[0][1]} veces')
else:
    print(
        f'La letra mas repetida es la "{letra_repetida_ordenada[0][0]}" '
        f'que se repite {letra_repetida_ordenada[0][1]} veces')
