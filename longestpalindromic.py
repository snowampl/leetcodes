from collections import defaultdict
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """


        return self.get_max(0, len(s)-1, s)


    def get_max(self, i,j, s):
        if i > j:
            return 0
        if i == j:
            return 1


        return max(self.get_max(i, j-1, s), 2 + self.get_max(i+1,j-1,s))






so = Solution()
print(so.longestPalindromeSubseq('abcdefghgfedcba'))
