from collections import defaultdict, Counter
from typing import List


def intersect_one(nums1: List[int], nums2: List[int]) -> List[int]:
    unique_nums1 = defaultdict(int)
    unique_nums2 = defaultdict(int)

    for num in nums1:
        unique_nums1[num] += 1

    for num in nums2:
        unique_nums2[num] += 1

    result = []

    for num in unique_nums1:
        if num in unique_nums2:
            count = min(unique_nums1[num], unique_nums2[num])

            for i in range(count):
                result.append(num)

    return result


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    unique_nums1 = {}
    result = []

    for num in nums1:
        unique_nums1[num] = unique_nums1.get(num, 0) + 1

    for num in nums2:
        if unique_nums1.get(num, 0) != 0:
            result.append(num)
            unique_nums1[num] -= 1

    return result


def intersect_two(nums1: List[int], nums2: List[int]) -> List[int]:
    counts = Counter(nums1)
    result = []

    for num in nums2:
        if counts[num] > 0:
            result += num,
            counts[num] -= 1

    return result


def intersect_three(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()
    i1 = i2 = 0
    result = []

    while True:
        try:
            if nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums2[i2] > nums1[i1]:
                i1 += 1
            else:
                result.append(nums1[i1])
                i1 += 1
                i2 += 1
        except IndexError:
            break

    return result


result = intersect([4, 9, 4, 5], [9, 4, 9, 8, 4])
print(result)
