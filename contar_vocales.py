# Python Program to Count the Number of Each Vowel in a sentence
vocales = 'aeiou'
oracion = input("ingrese una oracion para contar sus vocales: ").lower()

cuenta = {x:0 for x in vocales}

for x in oracion:
    if x in cuenta:
        cuenta[x]+=1
print(cuenta)
