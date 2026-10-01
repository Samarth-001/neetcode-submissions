class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        perimeter = 0
        # print(len(grid[0]))

        for i in range(len(grid)):
            for j in range(len(grid[i])):

                el = grid[i][j]
                if el==0:
                    continue

                side = 0

                print(i, j)

                if j==len(grid[i])-1 or grid[i][j+1] == 0:
                    side+=1
                if (i == len(grid)-1) or grid[i+1][j] == 0:
                    side+=1
                if j==0 or grid[i][j-1] == 0:
                    side+=1
                if i==0 or grid[i-1][j] == 0:
                    side+=1                  
                
                perimeter+= side
        
        # print(perimeter)
        return perimeter