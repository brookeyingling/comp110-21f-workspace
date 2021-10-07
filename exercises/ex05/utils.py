"""List utility functions part 2."""

__author__ = "730405432"

# Define your functions below


def only_evens(numbers: list[int]) -> list[int]:
    """Find the evens in a list of numbers given by the user."""
    evens: list[int] = list()
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens    


def sub(a_list: list[int], first: int, last: int) -> list[int]:
    """Generate a subset list of a list given by the user."""
    i: int = 0
    substitutionlist: list[int] = []
    if len(a_list) == 0 or first > len(a_list) or last <= 0 or first >= last:
        return substitutionlist
    if first < 0:
        first = 0
    if last > len(a_list):
        last = (len(a_list) - 1)
    while i < len(a_list):
        if first <= a_list[i] < last:
            substitutionlist.append(a_list[i])
        i += 1
    return substitutionlist


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """Combine two lists inputed by the user into one long list."""
    combinedlist: list[int] = []
    for insides in list_1:
        combinedlist.append(insides)
    for insides in list_2:
        combinedlist.append(insides)
    return combinedlist