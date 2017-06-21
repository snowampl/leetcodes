from collections import defaultdict
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        if len(nums)%2 == 0:
            return True
        return self.dp(0, len(nums)-1, nums) > sum(nums)/2

    def dp(self,i,j, nums):
        if i == j:
            return nums[i]
        a = nums[i] + min(self.dp(i+1,j-1, nums), self.dp(i+2, j, nums))
        b = nums[j] + min(self.dp(i, j-2, nums), self.dp(i+1, j-1, nums))
        return max(a,b)

so = Solution()
print so.PredictTheWinner([1,5,233,2])







