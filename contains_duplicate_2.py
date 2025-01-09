def contains_nearby_duplicate(nums, k):
    seen = set()
    for i, n in enumerate(nums):
        if n in seen:
            return True
        seen.add(n)
        if len(seen) > k:
            seen.remove(nums[i-k])
    return False

nums = [1,2,3,1]
k = 3

print(contains_nearby_duplicate(nums, k))