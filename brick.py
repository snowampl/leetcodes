from collections import defaultdict
import operator

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        if len(wall) == 0:
            return 0
        countedge = defaultdict(int)
        for i in range(0, len(wall)):
            total = 0
            for j in range(0, len(wall[i])):
                total += wall[i][j]
                countedge[total] += 1
        sorted_count = sorted(countedge.items(), key=operator.itemgetter(1), reverse=True)
# need to delete the end edge
        if len(sorted_count) == 1:
            return len(wall)
        else:
            return len(wall) - sorted_count[1][1]