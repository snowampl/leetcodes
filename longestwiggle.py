class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        The critical point is : the last point of a subsequence must be in the optimal sequence
        we can prove that the last element of any subset from 0 to i, num[i] must be in the optimal solution.
        
        for example [1,3, 2, 4, 5] if there is a subsquence with continue upwards, 
        then the last up always can replace the previous up element to be the optimal one. That is why it can be 
        solved by DP.
        """
        up = [0] * len(nums)
        down = [0] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                up[i] = up[i-1]
                down[i] = down[i-1]
        return max(up[-1], down[-1]) + 1


so = Solution()
print so.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8])

