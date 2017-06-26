import math
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        current = 9
        ans = 10

        for j in range(2, n+1):
            if j > 10:
                break
            current = current * (11 - j)
            ans += current

        return ans
