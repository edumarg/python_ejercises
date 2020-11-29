# Python program to check if the number provided by the user is an Armstrong number or not

# A positive integer is called an Armstrong number of order n if
# abcd... = an + bn + cn + dn + ...

# In case of an Armstrong number of 3 digits, the sum of cubes of each digits is equal to the number itself. For example:
# 153 = 1*1*1 + 5*5*5 + 3*3*3  // 153 is an Armstrong number.

entrada = input('introducs un numero para comprovar si es un numero AMSTRONG: ')
try:
    numero = int(entrada)
except ValueError:
    print('Valor invalido, por favor introdusca un numero')
else:
    count = 0
    n= len(entrada)
    for x in entrada:
        count += int(x)**n
    if count == numero:
        print(f'{entrada} es un numero AMSTRONG')
    else:
        print(f'{entrada} NO es un numero AMSTRONG')

# Python Program to Find Armstrong Number in an Interval
try:
    inferior = int(input('introdusca limite inferior del rango para verificar numeros AMSTRON: '))
    superior = int(input('introdusca limite superior del rango para verificar numeros AMSTRON: '))
except ValueError:
    print('Valores de limites incorectos, por favor introdusca numero enteros')
else:
    for num in range(inferior,superior+1):
        count = 0
        n = len(str(num))
        for x in str(num):
            count += int(x) ** n
        if count == num:
            print(f'{num} es un numero AMSTRONG')
        # else:
        #     print(f'{num} NO es un numero AMSTRONG')
