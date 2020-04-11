class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        counter = {}
        counts = 0
        for i in arr:
            counter[i] = counter.get(i, 0) + 1
        for i in counter:
            if i + 1 in counter:
                counts += counter[i]
        return counts
