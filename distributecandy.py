from collections import defaultdict
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy = defaultdict(int)
        for item in candies:
            candy[item] += 1

        return min(len(candies)/2, len(candy.keys()))
