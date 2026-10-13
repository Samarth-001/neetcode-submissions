
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        edges = []

        for i in range(n):
            for j in range(i+1,n):
                xi, yi = points[i]
                xj, yj = points[j]

                cost = abs(xi-xj) + abs(yi-yj)

                edges.append([cost,i,j])
        
        edges.sort()
        # print(edges)

        parent = list(range(n))
        size = [1]*n

        # print(parent)

        def find(x):
            if parent[x]!=x:
                return find(parent[x])
            return x
        
        def union(a,b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False
            
            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA
            
            parent[rootB] = rootA
            size[rootA] += size[rootB]

            return True 

        total_cost = 0
        edges_used = 0

        for cost,a,b in edges:
            if union(a,b):
                total_cost += cost
                edges_used += 1

                if edges_used == n-1:
                    break

        return total_cost





