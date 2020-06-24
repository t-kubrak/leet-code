def reverse_1(x: int) -> int:
    if x > 2 ** 31 - 1 or x < -2 ** 31:
        return 0

    result = list(str(x))
    result = result[1:] if x < 0 else result

    for i in range(len(result) // 2):
        result[i], result[~i] = result[~i], result[i]

    sign = "-" if x < 0 else ""
    result = sign + "".join(result)

    if int(result) > 2 ** 31 - 1 or int(result) < -2 ** 31:
        return 0

    return int(result)


def reverse_2(x: int) -> int:
    if not -(2 ** 31) - 1 < x < 2 ** 31:
        return 0

    sign = -1 if x < 0 else 1

    result = sign * int(str(abs(x))[::-1])

    return result if -(2 ** 31) - 1 < result < 2 ** 31 else 0


def reverse(x: int) -> int:
    result = 0

    if x < 0:
        sign = -1
        x = -x
    else:
        sign = 1

    while x:
        # pop
        pop = x % 10
        x //= 10

        result = result * 10 + pop  # push

    return result * sign if -pow(2, 31) <= result * sign <= pow(2, 31) - 1 else 0


result = reverse(-1023)
print(result)
