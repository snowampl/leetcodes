class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.maxvalue = [-1] * len(prices)

        result = self.helper(prices, len(prices) - 1)

        return result


    def helper(self, prices, k):



        if k <= 0:
            return 0

        if k == 1:
            return max(0, prices[k] - prices[k-1])

        if self.maxvalue[k] >= 0:
            return self.maxvalue[k]

        temp = 0

        for i in range(k-1, -1, -1):
            temp = max(self.helper(prices, i-2) + prices[k] - prices[i], temp)
        temp = max(temp, self.helper(prices, k-1))

        self.maxvalue[k] = temp

        return temp

so = Solution()
print so.maxProfit([1,2,4])
