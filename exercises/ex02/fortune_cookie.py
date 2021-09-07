"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730405432"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

fortune: int = randint(1, 100)
print("Your fortune cookie says...")
if 0 < fortune < 25:
    print("Life is going to take you for a ride, hop in and enjoy it!")
else:
    if 26 < fortune < 50:
        print("Your doubt is clouding your judgement, trust yourself!")
    if 51 < fortune < 75:
        print("Someone is going to come into your life and change it for the best.")
    if 76 < fortune < 100:
        print("Life is too precious, eat your cake and enjoy it too.")
print("Now go spread positive vibes!")