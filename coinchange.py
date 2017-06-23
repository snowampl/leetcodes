from collections import defaultdict
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.values = defaultdict(int)

        coins = sorted(coins)

        return self.helper(coins, amount)


    def helper(self, coins, amount):

        if self.values[amount] > 0:
            return self.values[amount]

        if amount % coins[-1] == 0:
            self.values[amount] = int(amount/coins[-1])
            return self.values[amount]

        if amount == 0:
            return 0
        if amount < 0:
            return -2
        minvalue = -1
        for i in range(len(coins)):
            temp = 1 + self.helper(coins, amount - coins[i])
            if (temp < minvalue and temp > 0) or (minvalue == -1 and temp>0):
                minvalue = temp
        if minvalue > 0:
            self.values[amount] = minvalue
        return minvalue

so = Solution()
print(so.coinChange([2, 5, 10, 1], 27))