import math
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        table = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            if i*i <= n:
                table[i*i] = 1
        if table[n] > 0:
            return table[n]

        for i in range(2, n+1):
            if table[i] == 0:
                table[i] = min([table[i-j*j] + 1 for j in range(1, int(math.sqrt(i))+1)])
        print table
        return table[n]

so = Solution()
print so.numSquares(12)
