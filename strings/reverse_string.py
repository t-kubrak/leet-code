from typing import List


def reverse_string(s: List[str]):
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]


input = ["H", "a", "n", "n", "a", "h"]
result = reverse_string(input)
print(result)