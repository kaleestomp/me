# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math
import random

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 1
    guess = 0

    print("\nWelcome to the guessing game! This time I will play it")    
    print("Nice, so a number between {0} and {1} ?".format(low, high))

    while True:
        random.seed(tries)
        guess = random.randint(low, high)
        print("I guessed {},".format(guess),)
        if guess > actual_number:
            high = guess - 1
            tries += 1
            print(f"oops. I'm wrong. It's too high. I will try for the {tries} times")
        elif guess < actual_number:
            low = guess + 1
            tries += 1
            print(f"opps. I'm wrong. It's too low. I will try for the {tries} times")
        else:
            print(f"AHA I got it! It's {guess}. Took me {tries} tries.")
            break

    # Write your code in here

    return {"guess": guess, "tries": tries}


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
