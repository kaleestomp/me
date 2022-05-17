TODO: Reflect on what you learned this week and what is still unclear.

1. always green light first before refactoring or adding fluff
2. learn how to use other people's code it's important.
3. try not to put input() inside functions; Minimize side effects to keep simple (if the context suits); the simpler the code the better

How does random generator work in python - I kept getting the same value without specifying seed()

"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

from asyncio.windows_events import NULL
from distutils.log import error
import random

def advancedGuessingGame():
"""Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _?")
    lowerBound = numberChecker(input("Enter the lower bound: "))
    upperBound = NULL
    while domainRangeNotValid(lowerBound, upperBound):
      upperBound = numberChecker(input("Now enter the highier bond: "))

    print("Nice, so a number between {0} and {1} ?".format(lowerBound, upperBound))

    actualNumber = random.randint(0, upperBound)

    guessed = False
    tryCount = 0

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print("You guessed {},".format(guessedNumber),)
        while(numberNotinRange(lowerBound, upperBound, guessedNumber)):
          guessedNumber = int(input("try another number: "))

        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
            tryCount += 1
        else:
            print("Too big, try again :'(")
            tryCount += 1

    if tryCount <= 6:
      print (f"WOW. Took you ONLY {tryCount} tries!")
    elif tryCount <= 12:
      print (f"Took you {tryCount} tries!")
    else:
      print (f"That was a drag... Took your {tryCount} tries. But oh well")

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!

def numberChecker(number):
errorCount = 0
try:
number = int(number)
return number
except:
errorCount += 1
if errorCount < 3:
number = numberChecker(input("try again. Use a number: "))
elif errorCount < 10:
number = numberChecker(input("I mean put in a NUMBER please"))
else:
print("You are not serious... Bye")
quit()

def domainRangeNotValid(low, high):
while high == NULL:
return True

while low >= high and high != NULL:
errorCount = 0
if errorCount < 3:
print(f"please put in a higher bond - meaning highier than {low}. Try again?")
errorCount += 1
elif errorCount <= 10:
print(f"Let me explain: you need a high number and a lower number to form a range\
 where you can guess a random number inbetween. Your low number is {low},\
 your low number can't be the same. And don't make it hard for yourself. \
 Use whole number. Try again?")
else:
print("You are not serious... Bye")
quit()
return True

while high - low <= 2 and high != NULL:
print("you are making it way too easy...try again")
return True

return False

def numberNotinRange(low, high, number):
while(number > high or number < low):
print("your number if out of bound. Try anthoer one")
return True
return False
if **name** == "**main**":
print(advancedGuessingGame())
