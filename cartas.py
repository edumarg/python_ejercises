# Python program to shuffle a deck of card using the module random and draw 5 cards

# import modules
import random

while True:
   input("Press enter to Shuffle the card deck")
   numeros = range(1,14)
   suits = ["Diamonds", "Heart", "Spades", "Clubs"]

   # make a deck of cards
   deck =[]
   for n in numeros:
      for s in suits:
         deck.append((n,s))

   random.shuffle(deck)

   # draw five cards
   print("You got:")
   for i in range(5):
      print(deck[i][0], "of", deck[i][1])

   option = input("Shuffle Again? (y/n) ")
   if option.lower() == 'n':
      break
