class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        strs_len = []
        for item in strs:
            temp = map(lambda x: 1 if x=='1' else 0, item)
            strs_len.append([len(item)-sum(temp), sum(temp)])
        print strs_len
        return self.get_max(strs_len, len(strs)-1, m, n)

    def get_max(self, strs_len, i, j, k):
        if i < 0 or k < 0 or j < 0:
            return 0
        a = 0
        if j >= strs_len[i][0] and k >= strs_len[i][1]:
            a = self.get_max(strs_len, i-1, j-strs_len[i][0], k-strs_len[i][1]) + 1
        b = self.get_max(strs_len, i-1, j, k)
        return max(a,b)


so = Solution()
print so.findMaxForm(["10","1","0"], 1, 1)