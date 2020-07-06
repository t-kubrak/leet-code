def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    for i in range(len(haystack) - len(needle) + 1):
        for j in range(len(needle)):
            if haystack[i + j] != needle[j]:
                break
            if j == len(needle) -1:
                return i

    return -1

result = str_str("hello", "ll")
print(result)
assert result == 2

result = str_str("aabaa", "baa")
print(result)
assert result == 2

result = str_str("aaa", "aaaa")
print(result)
assert result == -1

result = str_str("a", "a")
print(result)
assert result == 0

result = str_str("mississippi", "issipi")
print(result)
assert result == -1