class Solution(object):
    def ifconnect(self, char1, char2):
        if ord(char2) - ord(char1) == 1 or (ord(char1) == 122 and ord(char2) == 97):
            return True
        else:
            return False
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        count = []
        table = {k:[False]*len(p) for k in p}
        for i in range(len(p)):
            table[p[i]][i] = True
            count.append(p[i])
            for j in range(i-1, -1, -1):
                table[p[i]][j] = table[p[i-1]][j] and self.ifconnect(p[i-1], p[i])
                if table[p[i]][j]:
                    count.append(p[j:i+1])
        print(count)
        print(table['b'])
        return len(set(count))

so = Solution()
print(so.findSubstringInWraproundString('zab'))