"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        hm = {}
        visited = set()

        def dfs(node):
            visited.add(node.val)
            hm[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor.val not in visited:
                    dfs(neighbor)
                hm[node].neighbors.append(hm[neighbor])
        
        dfs(node)

        print(hm)

        return hm[node]        