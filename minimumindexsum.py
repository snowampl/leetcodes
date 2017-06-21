from collections import defaultdict
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sumoflist = defaultdict(list)
        for i in range(0, len(list1)):
            sumoflist[list1[i]].append(i)

        for i in range(0, len(list2)):
            sumoflist[list2[i]].append(i)

        minsum = 200000
        minkey = []
        for key in sumoflist.keys():
            if len(sumoflist[key]) == 2 and sum(sumoflist[key]) <= minsum:
                minsum = sum(sumoflist[key])
                minkey.append(key)
        return(minkey)
