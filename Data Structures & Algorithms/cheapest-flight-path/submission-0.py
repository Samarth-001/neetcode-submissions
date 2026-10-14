class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        cost = [float('inf')] * n
        cost[src] = 0

        for _ in range(k+1):

            new_cost = cost.copy()

            for s, e, price in flights:
                if cost[s] != float('inf'):
                    new_cost[e] = min(new_cost[e], cost[s] + price)

            cost = new_cost
        
        return cost[dst] if cost[dst] != float('inf') else -1