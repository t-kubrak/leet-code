def two_sum_brute_force(nums, target):
    for key, num in enumerate(nums):
        for key_two, num_two in enumerate(nums[key + 1:]):
            if num + num_two == target:
                return [key, key_two + key + 1]

    return None

def two_sum(nums, target):
    dict = {}

    for key, num in enumerate(nums):
        num_two = target - num

        if num_two not in dict:
            dict[num] = key
            continue

        return [dict[num_two], key]

    return None

result = two_sum([2, 7, 11, 15], 18)

print(result)