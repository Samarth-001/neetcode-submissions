class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        # Sort in reverse so pop() returns the smallest airport
        for source, destination in sorted(tickets, reverse=True):
            graph[source].append(destination)
        
        # print(graph)

        result = []
        def dfs(airport):
            while graph[airport]:
                dfs(graph[airport].pop())
            
            result.append(airport)
        
        dfs('JFK')

        return result[::-1]