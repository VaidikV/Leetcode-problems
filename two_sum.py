def two_sum(nums, target):
    hashMap = {}

    for i, v in enumerate(nums):
        diff = target - v

        if diff in hashMap:
            return [i, hashMap[diff]]
        hashMap[v] = i


nums = [2, 11, 7, 3]
target = 9

print(two_sum(nums, target))