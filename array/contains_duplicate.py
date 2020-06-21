from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


def contains_duplicate_two(nums: List[int]) -> bool:
    unique_nums = set()

    for num in nums:
        if num in unique_nums:
            return True

        unique_nums.add(num)


result = contains_duplicate([1, 2, 3, 1])
print(result)
