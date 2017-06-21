class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        if s is t's subsequence
        """
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True
        current = 0

        for i in range(0, len(t)):
            if t[i] == s[current]:
                current += 1
                if current == len(s):
                    return True
        return False

so = Solution()
print so.isSubsequence('abc', 'axbdc')

