from typing import List


def rotate_initial(nums: List[int], k: int) -> List[int]:
    for i in range(k):
        nums.insert(0, nums.pop())

    return nums


def rotate_brute_force(nums: List[int], k: int) -> List[int]:
    for i in range(k):
        previous = nums[-1]

        for j in range(len(nums)):
            nums[j], previous = previous, nums[j]

    return nums


def rotate(nums: List[int], k: int) -> List[int]:
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    k, n = k % len(nums), len(nums)

    if k:
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    return nums


result = rotate([1, 2, 3, 4, 5, 6, 7], 3)

print(result)
