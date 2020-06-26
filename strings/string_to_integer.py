def my_atoi(str: str) -> int:
    str = str.strip()

    if not str:
        return 0

    is_negative = False
    num = 0

    if str[0] == '-':
        is_negative = True
        str = str[1:]
    elif str[0] == '+' and len(str) > 1 and str[1].isdigit():
        str = str[1:]
    elif not str[0].isdigit():
        return 0

    for i in range(len(str)):
        if not str[i].isdigit():
            break

        num = num * 10 + int(str[i])

    if is_negative:
        num = -num

    if num > 2 ** 31 - 1:
        return 2 ** 31 - 1
    elif num < -2 ** 31:
        return -(2 ** 31)

    return num


result = my_atoi("+1")
print(result)
assert result == 1

result = my_atoi("+-2")
print(result)
assert result == 0

result = my_atoi("   -42")
print(result)
assert result == -42

result = my_atoi("4193 with words")
print(result)
assert result == 4193

result = my_atoi("words and 987")
print(result)
assert result == 0

result = my_atoi("-91283472332")
print(result)
assert result == -2147483648
