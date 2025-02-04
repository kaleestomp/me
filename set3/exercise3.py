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
    lowerBound = not_number_rejector("Enter the lower bound: ")
    upperBound = not_number_rejector("Now enter the highier bond: ")

    # while domainRangeNotValid(lowerBound, upperBound):
    #     upperBound = numberChecker(input("Enter a valid highier bond: "))

    print(f"Nice, so a number between {lowerBound} and {upperBound} ?")

    actualNumber = random.randint(lowerBound, upperBound)
    guessed = False
    tryCount = 1
    while not guessed:
        print("Guess a number: ")
        guessedNumber = super_asker(lowerBound, upperBound)
        print(f"You guessed {guessedNumber},")

        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            tryCount += 1
            print(f"{chastisePlayer01(tryCount)} Too small, try again :'(")
        else:
            tryCount += 1
            print(f"{chastisePlayer01(tryCount)} Too big, try again :'(")

    print(chastisePlayer02(tryCount))

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


def numberChecker(number):
    errorCount = 0
    while True:
        try:
            number = int(number)
            return number
        except:
            errorCount += 1
            if errorCount < 3:
                number = input("try again. Use a number: ")
            elif errorCount < 10:
                number = input("I mean put in a NUMBER please")
            else:
                print("You are not serious... Bye")
                quit()


def domainRangeNotValid(low, high):
    while low >= high:
        errorCount = 0
        if errorCount < 3:
            print(
                f"please put in a higher bond - meaning highier than {low}. Try again?"
            )
            errorCount += 1
        elif errorCount <= 10:
            print(
                f"Let me explain: you need a high number and a lower number to form a range\
        where you can guess a random number inbetween. Your low number is {low},\
        your low number can't be the same. And don't make it hard for yourself. \
        Use whole number. Try again?"
            )
        else:
            print("You are not serious... Bye")
            quit()
        return True

    while high - low <= 10:
        if high - low <= 1:
            print("this can't work dumb dumb")
            return True
        else:
            print("you are making it way too easy...give yourself a challeng")
            return True

    return False

    while number > high or number < low:
        print("your number if out of bound. Try anthoer one")
        return True
    return False


def chastisePlayer01(tryCount):
    if tryCount <= 3:
        return "Keep going!"
    elif tryCount <= 6:
        return "OH C'mon"
    elif tryCount <= 9:
        return "this is becoming a drag..."
    elif tryCount <= 12:
        return "this isnt your game is it..."
    elif tryCount <= 24:
        return "..."
    else:
        print("I have taken the liberty to end this torture for you")
        quit()


def chastisePlayer02(tryCount):
    if tryCount <= 3:
        return f"WOW! Took you ONLY {tryCount} tries!"
    elif tryCount <= 6 and tryCount > 3:
        return f"Took you {tryCount} tries."
    elif tryCount <= 9 and tryCount > 6:
        return f"That was a drag...Took you {tryCount} tries."
    else:
        return f"{tryCount} tries...Let's not do that again."


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    while True:
        try:
            n = input(message)
            inputNum = float(n)
            return inputNum
        except:
            print("give a proper number please: ")


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    Try to call at least one of the other functions to minimise the
    amount of code.
    """
    inputNum = NULL
    while inputNum > high or inputNum < low or inputNum == NULL:
        if inputNum > high:
            print("your number is too high")
        elif inputNum < low and inputNum != NULL:
            print("your number is too low")
        inputNum = not_number_rejector(
            f"please insert a number between {high} and {low}: "
        )
    return inputNum


if __name__ == "__main__":
    print(advancedGuessingGame())
