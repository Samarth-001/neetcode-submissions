class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def convert(grid, i ,j):
            grid[i][j] = 0

            check = 1

            if j+1<len(grid[i]) and grid[i][j+1] == 1:
                check+= convert(grid,i,j+1)
            if i+1<len(grid) and grid[i+1][j] == 1:
                check+= convert(grid,i+1,j)
            if i>0 and grid[i-1][j] == 1:
                check+= convert(grid,i-1,j)
            if j>0 and grid[i][j-1] == 1:
                check+= convert(grid,i,j-1)

            return check
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    print(ans)
                    ans = max(ans, convert(grid, i ,j))
        
        return ans