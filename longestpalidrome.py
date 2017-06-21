class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s)):
            table[i][i] = 1
            for j in range(i-1, -1,-1):
                if s[i] == s[j]:
                    if j+1 <= i-1:
                        table[j][i] = 2 + table[j+1][i-1]
                    else:
                        table[j][i] = 2
                else:
                        table[j][i] = max(table[j+1][i], table[j][i-1])

        return table[0][len(s)-1]

so = Solution()
print so.longestPalindromeSubseq('bbbab')