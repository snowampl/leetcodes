import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1 or num < 0:
            return False
        maxdiv = int(math.sqrt(num))
        total = 1
        for i in range(2, maxdiv + 1):
            if num % i == 0:
                total += i + num / i

        if total == num:
            return True
        else:
            return False
