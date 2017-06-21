from collections import defaultdict
import operator
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        countchar = defaultdict(int)
        for char in s:
            countchar[char] += 1

        sortedchar = sorted(countchar.items(), key=operator.itemgetter(1), reverse=True)
        result = 0
        flag = 0
        for item in sortedchar:
            if item[1] % 2 == 1:
                if flag == 0:
                    result += item[1]
                    flag = 1
                else:
                    result += item[1] - 1
            else:
                result += item[1]

        return result

def main():
    so = Solution()
    print(so.longestPalindrome("abccccdd"))

if __name__ == '__main__':
    main()



