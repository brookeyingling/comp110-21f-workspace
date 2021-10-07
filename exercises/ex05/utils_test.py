"""Unit tests for list utility functions."""

__author__ = "730405432"
# TODO: Uncomment the below line when ready to write unit tests
from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """Tests for a list that is empty."""
    assert only_evens([]) == []


def test_only_evens_odds() -> None:
    """Test the list for only odd numbers."""
    only_odds: list[int] = [1, 3, 5, 7]
    assert only_evens(only_odds) == []


def test_only_evens_evens() -> None: 
    """Tests for only the even numbers in the list."""
    only_even_evens: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert only_evens(only_even_evens) == [2, 4, 6, 8]


def test_sub_example() -> None:
    """Tests what and example list input should result in."""


def test_sub_two() -> None:
    """Tests what and example list input should result in."""


def test_sub_three() -> None:
    """Tests what and example list input should result in."""


def test_concat_empty() -> None:
    """Tests for a list that is empty."""
    list_1: list[int] = []
    list_2: list[int] = []
    assert concat(list_1, list_2) == []


def test_concat_normal_list() -> None:
    """Tests where two full lists are given."""
    list_1: list[int] = [7, 8, 9]
    list_2: list[int] = [21, 22, 23]
    assert concat(list_1, list_2) == [7, 8, 9, 21, 22, 23]


def test_concat_strange_list() -> None:
    """Tests for lists that have one of the lists empty."""
    list_1: list[int] = []
    list_2: list[int] = [21, 22, 23]
    assert concat(list_1, list_2) == [21, 22, 23]