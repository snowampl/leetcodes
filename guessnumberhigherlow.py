
class Solution(object):

    def getMoneyAmount(self, n):

        money = [[0] * (n+2) for i in range(0, n+2)]

        for i in range(1, n+1):
            money[i][i] = 0
            j = i
            for j in range(i-1, 0, -1):
                minvalue = 10000000
                for x in range(i, j-1, -1):
                    left = money[max(j, x-1)][j]
                    right = money[i][min(i, x+1)]
                    if x + max(left,right) < minvalue:
                        minvalue = x + max(left,right)
                money[i][j] = minvalue
        return money[n][1]




so = Solution()

print so.getMoneyAmount(20)







