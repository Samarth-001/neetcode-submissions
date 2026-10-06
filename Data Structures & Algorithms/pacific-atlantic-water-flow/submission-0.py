class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        def find(i,j, side):
            if side == "p":
                pacific.add((i,j))
            else: 
                atlantic.add((i,j))
            
            direction = [(-1,0),(1,0),(0,1),(0,-1)]

            for ni, nj in direction:
                ni += i
                nj += j

                if (ni>=0 and ni<len(heights)) and (nj>=0 and nj<len(heights[0])) and heights[ni][nj] >= heights[i][j]:
                    if side == "p" and (ni,nj) not in pacific:
                        find(ni,nj,side)
                    elif side == "a" and (ni,nj) not in atlantic: 
                        find(ni,nj,side)
            
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if i == 0 or j == 0:
                    find(i,j, "p")
                if (i == len(heights)-1) or (j == len(heights[0])-1):
                    find(i,j, "a")

        res=[]

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])
        
        return res