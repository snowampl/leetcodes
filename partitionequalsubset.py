class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        total = sum(nums)
        if total % 2 == 1:
            return False

        objective = int(total / 2)

        table = [[0] * (objective+1) for _ in range(len(nums))]

        for i in range(1,objective+1):
            if nums[0] < i:
                table[0][i] = 0
            else:
                table[0][i] = nums[0]
        for j in range(1, len(nums)):
            for i in range(1, objective+1):
                if i >= nums[j]:
                    table[j][i] = max(table[j-1][i-nums[j]] + nums[j], table[j-1][i])
                    if table[j][i] == objective:
                        return True

        print(table[len(nums)-1][objective])
        return False

so = Solution()
print(so.canPartition([1, 2,3,8]))



