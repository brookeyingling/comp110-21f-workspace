"""Utility functions."""

__author__ = "730405432"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Interpret the csv file."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Create/establish the column values."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(columnar_values: dict[str, list[str]], value: int) -> dict[str, list[str]]:
    """Produce a new column-based table with only the first N rows of data for each column."""
    result: dict[str, list[str]] = {}
    if value >= len(columnar_values):
        return columnar_values
    for column in columnar_values:
        first_row: list[str] = []
        for row in range(0, value):
            first_row.append(columnar_values[column][row])
        result[column] = first_row
    return result


def select(columns_table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based tab;e with only a specific subset of the og columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = columns_table[column]
    return result


def count(old_list: list[str]) -> dict[str, int]:
    """Create a new dictionary with unique key values and the frequency in which they appear."""
    result: dict[str, int] = {}
    for item in old_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def helper_function(values: dict[str, list[str]], first_column: str, second_column: str, responses: str) -> float:
    i: int = 0
    a: int = 0
    while i < len(values[first_column]):
        if values[first_column][i] == responses:
            a += int(values[second_column][i])
        i += 1
    b: dict[str, int] = count(values[first_column])
    return a / b[responses]