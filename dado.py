# Python program to illustrate a loop with condition at the bottom
# Roll a dice untill user chooses to exit
# import random module
import random
while True:
   input("Press enter to roll the dices")
   # get a number between 1 to 6
   num1 = random.randint(1, 6)
   num2 = random.randint(1,6)
   print("You got",num1 , '&', num2)
   option = input("Roll again?(y/n) ")
   # condition
   if option.lower() == 'n':
       break
