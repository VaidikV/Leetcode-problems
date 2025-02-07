class num_array(object):
    def __init__(self, nums):
        self.acc_nums = [0]
        for num in nums:
            self.acc_nums.append(self.acc_nums[-1] + num)

    def sum_range(self, left, right):
        return self.acc_nums[right+1] - self.acc_nums[left]



num_array = num_array([-2, 0, 3, -5, 2, -1])
print(num_array.sum_range(2,5))

