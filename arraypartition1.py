
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums) == 0:
            return 0
        total = 0
        i = 0
        while i < len(nums):
            total += min(nums[i], nums[i+1])
            i += 2

        return total


