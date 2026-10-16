class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mem = {}

        def find(i):
            if i>=n:
                return 0
            if i in mem:
                return mem[i]

            mem[i] = cost[i] + min(find(i+1), find(i+2))
            return mem[i]

        return min(find(0), find(1))