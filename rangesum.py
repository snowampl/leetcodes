class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums[0:]
        self.sumvalue = {}
        total = 0
        for i in range(0, len(self.nums)):
            total += self.nums[i]
            self.sumvalue[i] = total

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > 0:
            return self.sumvalue[j] - self.sumvalue[i-1]
        else:
            return self.sumvalue[j]





        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # param_1 = obj.sumRange(i,j)