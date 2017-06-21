class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        mini = m
        minj = n

        for item in ops:
            if item[0] < mini:
                mini = item[0]
            if item[1] < minj:
                minj = item[1]

        return (mini)*(minj)