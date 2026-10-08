class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree = [0] * numCourses
        graph = {}
        
        for req in prerequisites:
            graph.setdefault(req[1],[]).append(req[0])
            indegree[req[0]] +=1
        
        # print(graph)
        # print(indegree)

        queue = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        # print("queue:",queue)
        while queue:
            el = queue.popleft()
            res.append(el)

            if el in graph:
                for node in graph[el]:
                    indegree[node]-=1 
                    if indegree[node] == 0:
                        queue.append(node)
        # print(res)
        if len(res) == numCourses:
            return res
        return []