# Given a string. The task is to print all words with even length in the given string
def print_even_word(texto):
    texto = texto.split()
    print(texto)
    for word in texto:
        if len(word) % 2 == 0:
            print(f'la palabra -{word}- es una palabra con numero de letras par')


print_even_word((input(' intodusca una frase para imprimir las palabras con numero de letras par: ')))
