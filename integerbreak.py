class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        product = [i for i in range(0,n+1)]
        product[2] = 2
        if n == 2:
            return 1
        if n == 3:
            return 2
        for i in range(4, n+1):
            for j in range(i-1, 0, -1):
                product[i] = max(product[j] * product[i-j], product[i])

        print product
        return product[n]

so = Solution()
print so.integerBreak(5)



