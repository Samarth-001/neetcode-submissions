class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i,j])

        if not queue:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            return 0

        level = 0
        while queue:
            print(queue)
            level+=1
            for _ in range(len(queue)):
                i,j = queue.popleft()
                
                directions = [(0,1), (0,-1), (1,0), (-1,0)]

                for ni,nj in directions:
                    ni += i
                    nj += j
                    # print("for: ", ni,nj)

                    if ((ni>=0 and ni<len(grid)) and (nj>=0 and nj<len(grid[0]))) and grid[ni][nj] not in [0,2]:
                        grid[ni][nj] = 2
                        queue.append((ni,nj))


        # print(grid) 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return level-1