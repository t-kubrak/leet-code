def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0

    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)):
        search = ""

        try:
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    break

                search += haystack[i + j]
        except IndexError:
            return -1

        if search == needle:
            return i

    return -1


result = str_str("hello", "ll")
print(result)
assert result == 2

result = str_str("aaaaa", "bba")
print(result)
assert result == -1

result = str_str("aaa", "aaaa")
print(result)
assert result == -1

result = str_str("mississippi", "issipi")
print(result)
assert result == -1