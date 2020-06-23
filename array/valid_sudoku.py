from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    rows_valid = are_rows_valid(board)

    if not rows_valid:
        return False

    columns_valid = are_columns_valid(board)

    if not columns_valid:
        return False

    return True


def are_rows_valid(board: List[List[str]]) -> bool:
    for row in board:
        row_values_set = set()

        for value in row:
            if value == ".":
                continue
            elif value in row_values_set:
                return False

            row_values_set.add(value)

    return True


def are_columns_valid(board: List[List[str]]) -> bool:
    for column in range(len(board[0])):
        column_values_set = set()

        for row in range(len(board)):
            value = board[row][column]

            if value == ".":
                continue
            elif value in column_values_set:
                return False

            column_values_set.add(value)

    return True

input = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

result = is_valid_sudoku(input)
print(result)
