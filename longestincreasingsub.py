class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        table = [1] * len(nums)

        for i in range(len(nums)-2, -1, -1):
            temp = 1
            for j in range(i, len(nums)):
                if nums[j] > nums[i] and table[j] + 1 > temp:
                    temp = table[j] + 1
            table[i] = temp
        print table
        return max(table)


so = Solution()
print so.lengthOfLIS([1,3,6,7,9,4,10,5,6])
