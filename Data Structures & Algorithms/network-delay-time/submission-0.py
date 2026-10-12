class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = {}

        for ui, vi, ti in times:
            graph.setdefault(ui,[]).append((vi,ti))
        
        for i in range(1,n+1,1):
            graph.setdefault(i,[])
        
        dist = [float('inf')] * (n+1)
        dist[k] = 0
        
        heap = [(0,k)]
        print(graph)

        while heap:
            cost, node = heapq.heappop(heap)

            if node not in graph:
                continue
            
            if cost>dist[node]:
                continue

            for neighbor, edge_cost in graph[node]:

                new_cost = cost + edge_cost

                if new_cost<dist[neighbor]:
                    dist[neighbor] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor))
            
        print(dist)

        ans = 0
        for num in range(1,len(dist),1):
            if dist[num] == float('inf'):
                return -1
            ans = max(ans,dist[num])
        
        return ans