class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1 = len(num1)
        len2 = len(num2)

        result = ['0'] *  (max(len1, len2) + 1)
        len3 = max(len1, len2) + 1
        left = 0

        for i in range(0, min(len1, len2)):
            temp = int(num1[len1-i-1]) + int(num2[len2-i-1]) + left
            left = temp / 10
            temp = temp % 10
            result[len3-i-1] = str(temp)

        if len1 > len2:
            for i in range(min(len1, len2), len1):
                temp = int(num1[len1-i-1]) + left
                left = temp /10
                temp = temp % 10
                result[len3 - i-1] = str(temp)
            result[0] = str(left)

        elif len2 > len1:
            for i in range(min(len1, len2), len2):
                temp = int(num2[len2-i-1]) + left
                left = temp /10
                temp = temp % 10
                result[len3 - i - 1] = str(temp)
            result[0] = str(left)
        else:
            result[0] = str(left)

        if result[0] == '0':
            return ''.join(result[1:])
        else:
            return ''.join(result)

so = Solution()
print so.addStrings('6', '501')






