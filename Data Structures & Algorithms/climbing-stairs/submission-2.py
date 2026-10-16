class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}

        def find(i):
            if i==n:
                return 1
            
            if i>n:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = find(i+1)+find(i+2)
            return memo[i]

            # return find(i+1)+find(i+2)
        
        return find(0)