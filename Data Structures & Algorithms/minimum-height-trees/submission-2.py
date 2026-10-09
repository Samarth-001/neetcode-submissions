class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        graph = {}
        degree = [0]*n

        for edge in edges:
            graph.setdefault(edge[0],[]).append(edge[1])
            graph.setdefault(edge[1],[]).append(edge[0])

            degree[edge[1]] += 1
            degree[edge[0]] += 1

        print(graph)
        # print(degree)
        
        queue = deque()

        for i in range(len(degree)):
            if degree[i] == 1:
                queue.append(i)
        print(queue)
        
        while n>2:
            print(degree)

            for _ in range(len(queue)):
                el = queue.popleft()
                n-=1
                # print(el)

                for neighbor in graph[el]:
                    # print("here")
                    degree[neighbor]-=1
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        # print(queue)
        return list(queue)









