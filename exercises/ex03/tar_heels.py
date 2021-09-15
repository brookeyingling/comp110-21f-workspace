"""An exercise in remainders and boolean logic."""

__author__ = "730405432"


# Begin your solution here...
number: int = int(input("Enter a number: "))
if (number % 2 == 0) and (number % 7 == 0):
    print("TAR HEELS")
else:
    if (number % 7) == 0:
        print("HEELS")
    else:
        if (number % 2) == 0:
            print("TAR")
        else:
            print("CAROLINA")