class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        graph = {}

        for edge in edges:
            graph.setdefault(edge[0],[]).append(edge[1])
            graph.setdefault(edge[1],[]).append(edge[0])
        
        # print(graph)
        
        visited = set()
        
        def check(node):
            # print(visited)
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    check(neighbor)
        ans = 0
        for i in range(n):
            if i not in visited:
                # print("okay")
                ans+=1
                check(i)
        
        return ans