# Python Program to Sort Words in Alphabetic Order
oracion = input('introdusca una oracion para ordnar su palabras alfabeticametne: ').lower()
lista_palabras = oracion.split()
print(lista_palabras)
lista_palabras_ordenada = sorted(lista_palabras, key=lambda palabras: palabras)
print(lista_palabras_ordenada)
