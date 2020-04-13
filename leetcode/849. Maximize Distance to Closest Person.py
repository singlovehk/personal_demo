class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        first1 = seats.index(1)
        dis = 0
        prev1 = first1
        for ind, i in enumerate(seats[first1:]):
            if i == 1:
                dis = max(first1 + ind - prev1, dis)
                prev1 = ind + first1
        return max(dis //2, first1, len(seats) - prev1 - 1)
