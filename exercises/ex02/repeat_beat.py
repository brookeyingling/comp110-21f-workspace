"""Repeating a beat in a loop."""

__author__ = "730405432"


# Begin your solution here...
beat: str = input("What beat do you want to repeat? ")
howmanybeat: int = int(input("How many times do you want to repeat it? "))
space: str = ""
i: int = 0

if howmanybeat <= 0:
    print("No beat...")
    print((str(beat) + " ") * howmanybeat)
else:
    while i < howmanybeat:
        space = space + beat
        if i < howmanybeat - 1:
            space = space + " "
        i = i + 1
    print(space)