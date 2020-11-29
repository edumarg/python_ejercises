# # Given a list, write a Python program to swap first and last element of the list.
list_in = input('ingrese numeros de la lista para intercambiar primero y ultimo: ')
lista =list_in.split()
print(lista)
lista[0], lista[-1] = lista[-1], lista[0]
print('nueva lista')
print(lista)



#-----
# Como funcion
#-----
def swapp_first_last(lista_in):
    lista = lista_in.split()
    lista[0], lista[-1] = lista[-1], lista[0]
    return lista

print(swapp_first_last(input('ingrese numeros de la lista para intercambiar primero y ultimo: ')))