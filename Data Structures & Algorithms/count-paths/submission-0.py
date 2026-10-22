class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        mem = {}

        def find(i,j):
            if i == m-1 and j == n-1:
                return 1
            
            if i >= m or j>=n:
                return 0
            
            if (i,j) in mem:
                return mem[(i,j)]

            paths = find(i+1,j) + find(i,j+1)
            mem[(i,j)] = paths
            
            return paths
        
        return find(0,0)