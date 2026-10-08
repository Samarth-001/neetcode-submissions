class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n<=1:
            return True
        elif n>1 and edges == []:
            return False

        graph = {}

        for edge in edges:
            graph.setdefault(edge[0],[]).append(edge[1])
            graph.setdefault(edge[1],[]).append(edge[0])
        
        print(graph)
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)


            for neighbor in graph[node]:

                if neighbor == parent:
                    continue

                if dfs(neighbor, node) == False:
                    return False

            return True
        
        if dfs(0,-1) and len(visited) == n:
            return True
        return False