class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def convert(grid, i ,j):
            grid[i][j] = "0"

            if j<=len(grid[i])-2 and grid[i][j+1] == "1":
                grid = convert(grid, i ,j+1)
            if i<=len(grid)-2 and grid[i+1][j] == "1":
                grid = convert(grid, i+1 ,j)
            if i>0 and grid[i-1][j] == "1":
                grid = convert(grid, i-1 ,j)
            if j>0 and grid[i][j-1] == "1":
                grid = convert(grid, i ,j-1)

            return grid
        
        # print(grid)
        grp = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                if grid[i][j] == "1":
                    grp+=1
                    grid = convert(grid, i ,j)
        
        return grp