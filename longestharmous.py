from collections import defaultdict
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        series = defaultdict(int)
        maxlength = 0
        for item in nums:
            for key in series.keys():
                if abs(item - key) <= 1:
                    series[key] += 1
            if item not in series.keys():
                series[item] += 1

        for key in series.keys():
            if series[key] > maxlength:
                maxlength = series[key]

        return maxlength



def main():
    so = Solution()
    print(so.findLHS([1,1,1,1]))

if __name__ == '__main__':
    main()
