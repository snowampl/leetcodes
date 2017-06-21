class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        [23, 2, 6, 4, 7], 6
        """
        table = [0] * len(nums)
        table[0] = nums[0]
        table[1] = table[0] + nums[1]
        if table[1] % k == 0:
            return True
        for i in range(2, len(nums)):
            table[i] = table[i-1] + nums[i]
            if table[i] % k == 0 or table[i]%k == table[i-2]%k:
                return True

        return False

so = Solution()
print so.checkSubarraySum([23, 2, 6, 4, 7], 6)


class Solution(object):
    def checkSubarraySum(self, nums, k):
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in xrange(len(nums) - 1))
        mods, cum_sum_mod_k = {0: -1}, 0
        for i, n in enumerate(nums):
            cum_sum_mod_k = (cum_sum_mod_k + n) % k
            if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
                return True
            if cum_sum_mod_k not in mods:
                mods[cum_sum_mod_k] = i
        return False