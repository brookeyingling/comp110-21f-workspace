"""Finding duplicate letters in a word."""

__author__ = "730405432"
word: str = input("Enter a word: ")
i: int = 0
duplicate: int = 0
found: bool = False

while i < len(word):
    duplicate = i + 1
    while duplicate < len(word):
        if word[i] == word[duplicate]:
            found = True
            duplicate = duplicate + 1
        else:
            duplicate = duplicate + 1
    i = i + 1

print(("Found duplicate: ") + (str(found)))