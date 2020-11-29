# You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether
# it is too high, too low, or your number.

import random

high_limit = 100
low_limit = 1
guesses = 0
answer = ' '

input('Think of a number from 1 to 100 and I will try to guess it in the less amount of tries. Press enter when READY')

while True:
    guesses += 1
    number = random.randint(low_limit, high_limit)
    print(f'The number you are thinking is {number}? yes/no' )
    answer = input('>> ')
    if 'yes' in answer.lower():
        print(f'Good, it took me {guesses} tries')
        break
    elif 'no' in answer.lower():
        answer = input(f'Is the number your are thinking higher or lower than {number}? lower/higher ')
        if 'higher' in answer.lower():
            low_limit = number+1
        if 'lower' in answer.lower():
            high_limit = number-1
