nums = [3, 0 , 1]

def missing_number(nums):
    target_sum = sum(range(len(nums) + 1))
    nums_sum = sum(nums)
    return target_sum - nums_sum

print(missing_number(nums))