class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        maxvalue = num
        minvalue = 1

        if num == 1:
            return True

        i = num
        while True:
            i = i/2
            if i * i > num:
                maxvalue = min(i, maxvalue)
            elif i * i < num:
                minvalue = max(i, minvalue)
                break
            else:
                return True

        for i in range(minvalue, maxvalue+1):
            if i * i == num:
                return True

        return False
