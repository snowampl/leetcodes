from collections import defaultdict
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        nums = [1, 2, 3]
        target = 4

        The possible combination ways are:
            (1, 1, 1, 1)
            (1, 1, 2)
            (1, 2, 1)
            (1, 3)
            (2, 1, 1)
            (2, 2)
            (3, 1)
        """
        table = defaultdict(int)
        rtable = defaultdict(int)
        result = 0
        for i in range(len(nums)):
            if nums[i] == target:
                result += 1
            else:
                table[nums[i]] += 1

        while True:
            for key in table.keys():
                for i in range(len(nums)):
                    if key + nums[i] < target:
                        rtable[key + nums[i]] += table[key]
                    if key + nums[i] == target:
                        result += table[key]
            table = rtable
            rtable = defaultdict(int)
            if len(table.keys()) == 0:
                break

        return result



so = Solution()
print so.combinationSum4([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], 10)



