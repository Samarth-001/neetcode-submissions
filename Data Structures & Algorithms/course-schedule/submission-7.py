class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len(prerequisites) == 0:
            return True

        graph = {}

        for req in prerequisites:
            graph.setdefault(req[0],[]).append(req[1])
            graph.setdefault(req[1],[])
        
        # print(graph)

        def check(key):
            if key in path:
                return False
            if key in visited:
                return True
            
            visited.add(key)
            path.add(key)

            for neighbor in graph[key]:
                # if neighbor not in visited:
                if not check(neighbor):
                    return False
            
            path.remove(key)
            return True

        visited = set()
        for key in list(graph.keys()):
            path = set()
            if not check(key):
                return False
        
        return True