from typing import List


def rotate(matrix: List[List[int]]):
    rows = len(matrix)
    offsets = 0

    while rows - offsets > 3:
        offsets += 1

    for offset in range(offsets + 1):
        top_row = matrix[0 + offset][:]
        right_col = to_right(matrix, top_row, offset)
        bottom_row = to_bottom(matrix, right_col, offset)
        left_col = to_left(matrix, bottom_row, offset)
        to_top(matrix, left_col, offset)

    return matrix


def to_right(matrix, top_row, offset):
    right_col = []
    i = 0
    first = matrix[0 + offset][-1 - offset]

    for row in range(offset, len(matrix) - offset):
        right_col.append(matrix[row][-1 - offset])
        matrix[row][-1 - offset] = top_row[i + offset]
        i += 1

    matrix[-1 - offset][-1 - offset] = first

    return right_col


def to_bottom(matrix, right_col, offset):
    bottom_row = []
    i = len(right_col) - 1
    first = right_col[-1]

    for col in range(offset, len(matrix[-1]) - offset):
        bottom_row.append(matrix[-1 - offset][col])
        matrix[-1 - offset][col] = right_col[i]
        i -= 1

    bottom_row[-1] = first

    return bottom_row


def to_left(matrix, bottom_row, offset):
    left_col = []
    i = 0

    for row in range(offset, len(matrix) - offset):
        if row != 0 + offset and row < len(matrix) - 1 - offset:
            left_col.append(matrix[row][0])

        matrix[row][0 + offset] = bottom_row[i]
        i += 1

    return left_col


def to_top(matrix, left_col, offset):
    i = len(left_col) - 1

    for col in range(1 + offset, len(left_col) + 1 - offset):
        matrix[0 + offset][col] = left_col[i]
        i -= 1


matrix_2_2: List[List[int]] = [
    [1, 2],
    [3, 4]
]

matrix: List[List[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_4_4: List[List[int]] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
result = rotate(matrix_2_2)
print(result)
