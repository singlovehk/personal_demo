class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        dist = [float('inf')] * N
        dist[K-1] = 0
        for i in range(N):
            for time in times:
                u = time[0] - 1
                v = time[1] - 1
                need = time[2]
                dist[v] = min(dist[u] + need, dist[v]) 
        return -1 if float('inf') in dist else max(dist)
            
