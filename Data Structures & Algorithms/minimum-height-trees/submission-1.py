class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
            
        graph = {}

        for edge in edges:
            graph.setdefault(edge[0],[]).append(edge[1])
            graph.setdefault(edge[1],[]).append(edge[0])
        

        # print(graph)

        def heightCheck(node, parent):
            height = 0
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue

                height = max(height, heightCheck(neighbor, node))
            
            return height+1
        
        minH = n
        res={}

        for i in range(n):
            height = heightCheck(i, -1)
            res.setdefault(height,[]).append(i)
            minH = min(height,minH)
        
        # print(res)

        return res[minH]