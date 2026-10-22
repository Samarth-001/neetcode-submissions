class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if m == 0:
            return 0
        
        mem ={}

        def find(i,j):
            if i>=m or j>=n or obstacleGrid[i][j] == 1:
                return 0
                
            if i == m-1 and j == n-1:
                return 1
            
            if (i,j) in mem:
                return mem[(i,j)]

            paths = find(i+1,j) + find(i,j+1)
            mem[(i,j)] = paths

            return paths
        
        return find(0,0)