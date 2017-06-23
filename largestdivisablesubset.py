from collections import defaultdict
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        table = defaultdict(list)
        nums = sorted(nums)
        table[nums[0]] = [nums[0]]

        for i in range(1, len(nums)):
            largest = 0
            key = -1
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0 and len(table[nums[j]]) > largest:
                    largest = len(table[nums[j]])
                    key = j
            if key >= 0:
                table[nums[i]] = table[nums[key]] + [nums[i]]
            else:
                table[nums[i]] = [nums[i]]
        largest = 0
        lkey = -1

        for key in table.keys():
            if largest < len(table[key]):
                largest = len(table[key])
                lkey = key
        return table[lkey]




so = Solution()
print(so.largestDivisibleSubset([4, 8, 10, 240]))
