from typing import List


def to_right(matrix, top_row):
    right_col = []
    i = 0
    first = matrix[0][-1]

    for row in range(len(matrix)):
        right_col.append(matrix[row][-1])
        matrix[row][-1] = top_row[i]
        i += 1

    matrix[-1][-1] = first

    return right_col


def to_bottom(matrix, right_col):
    bottom_row = []
    i = 0
    first = right_col[-1]

    for col in range(len(matrix[-1])):
        bottom_row.append(matrix[-1][col])
        matrix[-1][~col] = right_col[i]
        i += 1

    bottom_row[-1] = first

    return bottom_row


def rotate(matrix: List[List[int]]):
    rows = len(matrix)
    columns = len(matrix[0])

    top_row = matrix[0]
    right_col = to_right(matrix, top_row)
    bottom_row = to_bottom(matrix, right_col)

    # for r in range(rows):
    #     for c in range(columns):
    #         current = matrix[r][c]
    #         matrix[r][c - 1]


matrix: List[List[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
result = rotate(matrix)
print(result)
