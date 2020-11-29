# crear una funcion para contar numero pares e impares de una lsita
def contar_par_impar(lista_in):
    lista = lista_in.split()
    par = 0
    impar = 0
    for i in lista:
        if int(i) % 2 == 0:
            par += 1
        elif int(i) % 2 != 0:
            impar += 1
    print(f'La lista tiene {par} nmeros pares y {impar} numeros impares')

contar_par_impar(input('ingrese lista para contar numeros pares e impares: '))
