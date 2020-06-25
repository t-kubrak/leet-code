import re


def is_palindrome_1(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()

    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return False

    return True


def is_palindrome_2(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if not re.fullmatch(r'[a-zA-Z0-9]+', s[left]):
            left += 1
        elif not re.fullmatch(r'[a-zA-Z0-9]+', s[right]):
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

    return True


result = is_palindrome_2("A man, a plan, a canal: Panama")
assert result == True
print(result)

result = is_palindrome_2("race a car")
assert result == False
print(result)
