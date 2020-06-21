from collections import defaultdict
from typing import List


def single_number_one(nums: List[int]) -> int:
    if not nums:
        return -1

    if len(nums) == 1:
        return nums[0]

    nums.sort()

    for i in range(1, len(nums) - 1, 2):
        current, previous = nums[i], nums[i - 1]

        if current != previous:
            return previous

    if nums[len(nums) - 1] != nums[len(nums) - 2]:
        return nums[len(nums) - 1]

    return -1


def single_number(nums: List[int]) -> int:
    unique_nums = defaultdict(int)

    for num in nums:
        unique_nums[num] += 1

    for key, val in unique_nums.items():
        if val == 1:
            return key


result = single_number([4, 1, 2, 1, 2])
print(result)
