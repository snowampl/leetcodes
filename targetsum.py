from collections import defaultdict
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == S or -1*nums[0] == S:
                return True
            else:
                return False
        temp = []
        temp.append(defaultdict(int))
        temp[0][nums[0]] += 1
        temp[0][-1*nums[0]] += 1
        for i in range(1, len(nums)):
            temp.append(defaultdict(int))
            for key in temp[i-1].keys():
                temp[i][key+nums[i]] += temp[i-1][key]
                temp[i][key-nums[i]] += temp[i-1][key]


        return temp[len(nums)-1][S]

so = Solution()
print so.findTargetSumWays([0,0,0,0,0,0,0,0,1], 1)
