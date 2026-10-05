class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i,j])
            
        print(queue)

        visited = set()
        
        # def multiBFS(i, j, level):
        #     level += 1
        #     visited[tuple([i,j])]=0

        #     # left
        #     if (j>0 and (grid[i][j-1] not in [-1, 0])) and ((tuple([i,j-1]) not in visited) or grid[i][j-1]>level):
        #         grid[i][j-1] = level
        #         multiBFS([i][j-1],level)
        #     # right
        #     if (j+1<len(grid[0])-1 and (grid[i][j+1] not in [-1, 0])) and ((tuple([i,j+1]) not in visited) or grid[i][j+1]>level):
        #     # if grid[i][j+1] not in [-1, 0]:
        #         grid[i][j+1] = level
        #         multiBFS([i][j+1],level)
        #     # up
        #     if (i>0 and (grid[i-1][j] not in [-1, 0])) and ((tuple([i-1,j]) not in visited) or grid[i-1][j]>level):
        #     # if grid[i-1][j] not in [-1, 0]:
        #         grid[i-1][j] = level
        #         multiBFS([i-1][j],level)
        #     # down
        #     if (i+1<(len(grid)-1) and (grid[i+1][j] not in [-1, 0])) and ((tuple([i+1,j]) not in visited) or grid[i+1][j]>level):

        #     # if grid[i+1][j] not in [-1, 0]:
        #         grid[i+1][j] = level
        #         multiBFS([i+1][j],level)
        
        level = 0
        while queue:
            level+=1
            # print(visited)
            for _ in range(len(queue)):
                el = queue.popleft()
                i = el[0]
                j = el[1]
                
                if (i+1,j) not in visited and i+1<=len(grid)-1 and grid[i+1][j] not in [-1, 0]:
                    grid[i+1][j] = level
                    queue.append([i+1,j])
                    visited.add((i+1,j))
                if (i-1,j) not in visited and i>0 and grid[i-1][j] not in [-1, 0]:
                    grid[i-1][j] = level
                    queue.append([i-1,j])
                    visited.add((i-1,j))
                if (i,j+1) not in visited and j+1<=len(grid[0])-1 and grid[i][j+1] not in [-1, 0]:
                    grid[i][j+1] = level
                    queue.append([i,j+1])
                    visited.add((i,j+1))
                if (i,j-1) not in visited and j>0 and grid[i][j-1] not in [-1, 0]:
                    grid[i][j-1] = level
                    queue.append([i,j-1])
                    visited.add((i,j-1))
                
        # return grid 



















