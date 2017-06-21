class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        A = [1, 2, 3, 4]
        return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
        """
        if len(A) < 3:
            return 0
        b1 = 0
        result = 0
        for i in range(2, len(A)):
            if A[i]-A[i-1] != A[i-1] - A[i-2]:
                current = i - b1
                result += (current - 1) * (current - 2)/2
                b1 = i - 1
        current = i - b1 + 1
        result += (current - 1)*(current - 2)/2
        return result

so = Solution()
print so.numberOfArithmeticSlices([1,2,3,4, 6, 7, 8])


