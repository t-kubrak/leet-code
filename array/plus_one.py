from typing import List


def plus_one(digits: List[int]) -> List[int]:
    number = ''

    for digit in digits:
        number += str(digit)

    number = int(number)
    number += 1
    number = str(number)

    return list(map(lambda num: int(num), number))


result = plus_one([9])
print(result)

