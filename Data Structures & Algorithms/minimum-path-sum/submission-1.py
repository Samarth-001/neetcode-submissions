class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        mem = {}

        def find(i,j):

            if i == m-1 and j == n-1:
                return grid[m-1][n-1]
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            if i == m-1:
                pathsum = find(i,j+1) + grid[i][j]
            elif j == n-1:
                pathsum = find(i+1,j) + grid[i][j]
            else:
                pathsum = min(find(i+1,j), find(i,j+1)) + grid[i][j]

            mem[(i,j)] = pathsum
            return pathsum
        
        return find(0,0)