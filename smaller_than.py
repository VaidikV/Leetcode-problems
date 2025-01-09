from operator import index

nums = [8,1,2,2,3]

def smaller_than(nums):
    temp = sorted(nums)
    d = {}

    for i in temp:
        if i not in d:
            d[i] = temp.index(i)

    ret = []
    for i in nums:
        ret.append(d[i])

    return ret

print(smaller_than(nums))