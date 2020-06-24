from collections import Counter


def first_unique_char(s: str) -> int:
    chars_dict = {}

    for char in s:
        chars_dict[char] = chars_dict.get(char, 0) + 1

    for key, char in enumerate(s):
        if chars_dict[char] == 1:
            return key

    return -1


def first_unique_char_2(s: str) -> int:
    count = Counter(s)

    for idx, ch in enumerate(s):
        if count[ch] == 1:
            return idx

    return -1


result = first_unique_char("loveleetcode")
print(result)
