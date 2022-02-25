import random
from typing import Sequence

print("Hello, what is your name?")
name = input()
secretNum = random.randint(1,20)
print("Well, " + name + ", I am thinking of a number between 1 and 20")

guess = 0
for guessesTaken in range(1,7):
  print("Take a guess.")
  try: 
    guess = int(input())
    if guess < secretNum:
      print("Too low")
    elif guess > secretNum:
      print("Too high")
    else:
      break
  except ValueError:
    print("That's not a number")


if guess == secretNum:
  print("Good job " + name + "! You got it right in " + str(guessesTaken) + " guesses")
else:
  print("Nupe, the number was " + str(secretNum))