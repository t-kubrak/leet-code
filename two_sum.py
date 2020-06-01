def twoSum(nums, target):
    for key, num in enumerate(nums):
        for key_two, num_two in enumerate(nums[key + 1:]):
            if num + num_two == target:
                return [key, key_two + key + 1]

    return None

result = twoSum([2, 7, 11, 15], 26)

print(result)