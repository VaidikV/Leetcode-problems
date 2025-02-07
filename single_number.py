def singleNumber(nums) -> int:
    xor = 0
    for i in nums:
        xor ^= i
    return xor

