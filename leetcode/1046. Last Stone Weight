class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = sorted(stones)
        length = len(stones)
        def bisect(li, num):
            lo = 0
            hi = len(li)
            while lo < hi:
                mid = (lo + hi) // 2
                if li[mid]< num:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        while len(stones) > 1:
            smashed = stones[-1] - stones[-2]
            stones = stones[:-2]
            if smashed != 0:
                stones.insert(bisect(stones,smashed), smashed)
            
        return 0 if len(stones) == 0 else stones[0]
