class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost = float('inf')
        profit = 0
        prev = -1
        for cur in prices:
            if prev> cur:
                profit += prev - cost
                cost = cur
            else :
                cost = min(cur, cost) 
            prev = cur
        profit += max(cur - cost, 0)
        return profit
