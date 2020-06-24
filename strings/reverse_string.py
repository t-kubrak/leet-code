from typing import List


def reverse_string(s: List[str]) -> None:
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]


def reverse_string_2(s: List[str]) -> None:
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1


def reverse_string_3(s: List[str]) -> None:
    def reverse(left, right):
        if left < right:
            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)

    reverse(0, len(s) - 1)

input = ["H", "a", "n", "n", "a", "h"]
reverse_string(input)
print(input)
