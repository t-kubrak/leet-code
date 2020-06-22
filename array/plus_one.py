from typing import List


def plus_one(digits: List[int]) -> List[int]:
    number = ''

    for digit in digits:
        number += str(digit)

    number = int(number)
    number += 1
    number = str(number)

    return list(map(lambda num: int(num), number))


def plus_one_v_2(digits: List[int]) -> List[int]:
    if len(digits) == 0:  # one digit case
        digits = [1]
    elif digits[-1] == 9:
        digits = plus_one_v_2(digits[:-1])
        digits.append(0)
    else:
        digits[-1] += 1

    return digits


def plus_one_v_3(digits: List[int]) -> List[int]:
    for i in range(len(digits)):
        if digits[~i] < 9:
            digits[~i] += 1
            return digits

        digits[~i] = 0

    return [1] + digits


result = plus_one([9, 9])
print(result)
