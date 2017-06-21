class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        i = 1
        while True:
            if n > i * 9 * int( pow(10, i-1)):
                n -= i * 9 * int(pow(10, i-1))
                i += 1
            else:
                break

        temp = n / i
        left = n % i

        if left == 0:
            result = int(str(pow(10, i-1) + temp - 1)[-1])
        else:
            result = int(str(pow(10, i-1) + temp)[left - 1])

        return result

so = Solution()
print(so.findNthDigit(3))
