from collections import defaultdict
from typing import List


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
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


result = intersect([4, 9, 4, 5], [9, 4, 9, 8, 4])
print(result)
