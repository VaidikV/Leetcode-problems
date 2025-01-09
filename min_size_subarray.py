def minSubArrayLen(int, nums):
    l = 0
    total = 0
    res = float('inf')

    for r in range(len(nums)):
        total += nums[r]

        while total >= int:
            res = min(res, r-l + 1)
            total -= nums[l]
            l += 1

    if res == float('inf'):
        return 0
    else:
        return res

target = 7
nums = [2,3,1,2,4,3]

print(minSubArrayLen(7, nums))