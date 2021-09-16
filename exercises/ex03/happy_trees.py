"""Drawing forests in a loop."""

__author__ = "730405432"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
number: int = int(input("Depth: "))
space: str = " "
i: int = 0

while i < number:
    i = i + 1
    print(TREE * i)