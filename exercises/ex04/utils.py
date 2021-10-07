"""List utility functions."""

<<<<<<< HEAD
__author__ = "730405432"


def all(numbers: list[int], number: int) -> bool:
    """Determine whether number is equal to the list numbers."""
    i: int = 0
    if len(numbers) == 0:
        return False
    else:
        while i < len(numbers):
            if numbers[i] != number:
                return False
            else:
                i += 1
        return True


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Determining whether or not two lists are equal."""
    i: int = 0
    b: int = 0
    if len(first_list) != len(second_list):
        return False
    while i < len(first_list):
        if first_list[i] != second_list[b]:
            return False
        else:
            i += 1
            b += 1
    return True


def max(input: list[int]) -> int:
    """Determing what the maximum value is in a given list of integers."""
    i: int = 0
    b: int = 0
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    while len(input) > i:
        if input[i] > input[b]:
            b += 1
            return input[i]
        else:
            i += 1
            return input[b]
=======
__author__ = "123456789"


# TODO: Implement your functions here.
>>>>>>> 75d5a25d0b84063cbf6a8cc58cc71c34269e73d8
