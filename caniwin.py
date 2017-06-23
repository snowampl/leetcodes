class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if (maxChoosableInteger)*(maxChoosableInteger+1)/2 < desiredTotal:
            return False

        if (maxChoosableInteger)*(maxChoosableInteger+1)/2 >= 2 * desiredTotal:
            return True

        self.memo = {}

        items = [i for i in range(1, maxChoosableInteger+1)]
        return self.helper(items, desiredTotal)

    def helper(self, items, target):

        if nums[-1] >= target:
            return True

        if str(nums) in self.memo:
            return self.memo[str(nums)]

        for i in range(len(items)):
            if not self.helper(nums[:i]+nums[i+1:], target-nums[i]):
                self.memo[str(nums)] = True
                return True
        self.memo[str(nums)] = False
        return False
