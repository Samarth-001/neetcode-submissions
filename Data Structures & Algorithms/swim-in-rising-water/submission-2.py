class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        dist = [[float('inf')]*len(grid[0]) for _ in range(len(grid))]
        dist[0][0] = grid[0][0]
            
        heap = [(grid[0][0],0,0)]

        while heap:
            # print(heap)
            time, i, j = heapq.heappop(heap) 

            if (i,j) == (len(grid)-1, len(grid[0])-1):
                return time

            directions = [(0,1),(0,-1),(1,0),(-1,0)]
            
            for k,l in directions:
                # print("here")
                ni=i+k
                nj=j+l

                if 0<=ni<len(grid) and 0<=nj<len(grid[0]):
                    if time>dist[ni][nj]:
                        continue

                    # print("here")
                    new_time = max(time, grid[ni][nj])
                    if new_time<dist[ni][nj]:
                        heapq.heappush(heap, (new_time, ni, nj))
                        dist[ni][nj] = new_time
        # print(dist)