class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix[0])
        n = len(matrix)
        
        ans = [[float('inf') for i in range(m)] for i in range(n)]
        
        for i in range(0, n):
            for j in range(0, m):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    ans[i][j] = 1 + (min(ans[min(i+1, n - 1)][j],
                                         ans[max(i-1, 0)][j],
                                         ans[i][max(j-1,0)],
                                        ans[i][min(j+1,m - 1)]))
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1 ):
                if matrix[i][j] == 0:
                    ans[i][j] = 0
                else:
                    ans[i][j] = 1 + (min(ans[min(i+1, n - 1)][j],
                                         ans[max(i-1, 0)][j],
                                         ans[i][max(j-1,0)],
                                        ans[i][min(j+1,m - 1)]))
        return ans
