class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        graph = {}

        def checkReachable(a,b):
            visited.add(a)
            if a == b:
                return True
            
            for neighbor in graph.get(a,[]):
                 if (neighbor not in visited) and checkReachable(neighbor,b):
                    return True
            return False


        for a,b in edges:
            visited = set()
            if not checkReachable(a,b):
                graph.setdefault(a,[]).append(b)
                graph.setdefault(b,[]).append(a)
            else:
                return [a,b]