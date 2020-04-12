class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        prev= prices[0]
        for cur in prices[1:]:
            profit += max(cur - prev, 0)
            prev = cur
        return profit
