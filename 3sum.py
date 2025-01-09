from logging import currentframe


def three_sum(nums):
    triplets = []
    nums.sort()
    for i, v in enumerate(nums):
        if i > 0 and v == nums[i-1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            current_sum = v + nums[left] + nums[right]

            if current_sum > 0:
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                triplets.append([v, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
    return triplets


nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))