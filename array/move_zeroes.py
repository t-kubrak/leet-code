from typing import List


def move_zeroes_one(nums: List[int]) -> None:
    zeroes = []
    other = []

    for num in nums:
        if num == 0:
            zeroes.append(num)
        else:
            other.append(num)

    return other + zeroes


def move_zeroes_two(nums: List[int]) -> None:
    for i in range(len(nums)):
        if nums[i] == 0:
            j = 0
            while i + j < len(nums) - 1 and nums[i + j] == 0:
                j += 1

            nums[i], nums[i + j] = nums[i + j], 0

            if i + j == len(nums) - 1:  # break the loop if the rest are zeroes
                break

    return nums


def move_zeroes_three(nums: List[int]) -> None:
    zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero], nums[i] = nums[i], nums[zero]
            zero += 1

    return nums


def move_zeroes_four(nums: List[int]) -> None:
    zeroes = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            zeroes += 1
        elif zeroes > 0:
            nums[i - zeroes], nums[i] = nums[i], 0

    return nums


result = move_zeroes_three([0, 1, 0, 0, 5])
print(result)
