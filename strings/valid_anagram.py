def is_anagram_1(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return sorted(s) == sorted(t)


def is_anagram_2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    chars = {}

    for i in range(len(s)):
        chars[s[i]] = chars.get(s[i], 0) + 1
        chars[t[i]] = chars.get(t[i], 0) - 1

    for char, count in chars.items():
        if count != 0:
            return False

    return True


result = is_anagram_2("anagram", "nagaram")
assert result == True
print(result)

result = is_anagram_2("rat", "car")
assert result == False
print(result)
