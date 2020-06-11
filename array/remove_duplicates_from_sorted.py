def removeDuplicates(nums):
    if len(nums) == 0:
        return 0

    unique_index = 1

    for i in range(len(nums) - 1):
        current = nums[i]
        next = nums[i + 1]

        if current != next:
            nums[unique_index] = next
            unique_index += 1

    nums = nums[:unique_index]

    return unique_index

result = removeDuplicates([0, 1, 1, 1, 2])

print(result)

