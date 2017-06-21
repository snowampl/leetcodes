class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        nums_sort = sorted(nums)
        total = 0
        for i in range(1, len(nums_sort)):
            total += nums_sort[i] - nums_sort[0]

        return total
