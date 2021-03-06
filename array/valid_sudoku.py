from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    return are_rows_valid(board) and \
        are_columns_valid(board) and \
        are_squares_valid(board, 3)


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


def are_squares_valid(board: List[List[str]], offset_size: int) -> bool:
    for row_offset in range(0, len(board), offset_size):
        for column_offset in range(0, len(board), offset_size):
            square_values_set = set()

            for row in range(0 + row_offset, len(board)):
                if row == row_offset + offset_size:
                    break

                for column in range(0 + column_offset, len(board[0])):
                    if column == column_offset + offset_size:
                        break

                    value = board[row][column]

                    if value == ".":
                        continue
                    elif value in square_values_set:
                        return False

                    square_values_set.add(value)

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
