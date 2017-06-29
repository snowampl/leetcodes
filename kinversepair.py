class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        (n+1, k) is equal (n,k)+(n, k-1)+(n, k-2)+...(n,k-n)
        """
        result = [[0] * (k+1) for _ in range(n)]
        result[0][0] = 1
        for i in range(1, n):
            for j in range(k+1):
                if j > 0:
                    result[i][j] = result[i][j-1] + result[i-1][j]
                    if j - i > 0:
                        result[i][j] = result[i][j] - result[i-1][j-i-1]
                else:
                    for m in range(j, max(j-i-1, -1), -1):
                        result[i][j] += result[i-1][m]

                result[i][j] = result[i][j] % 1000000007
        print result
        return result[n-1][k]


so = Solution()
print so.kInversePairs(3, 1)