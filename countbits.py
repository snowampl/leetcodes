class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        if num == 0:
            return 0
        if num == 1:
            return [0, 1]
        if num == 2:
            return [0, 1, 1]

        result[0] = 0
        result[1] = 1
        result[2] = 1
        for i in range(3, num + 1):
            if i % 2 == 1:
                result[i] = result[i-1] + 1
            else:
                result[i] = result[int((i-1)/2) + 1]

        return result



so = Solution()
print so.countBits(5)