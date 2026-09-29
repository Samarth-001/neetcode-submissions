import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x = point[0]
            y = point[1]

            dist = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
            heapq.heappush(heap, (dist, point))
        
        # print(heap)
        ans = []
        while k>0:
            ans.append(heapq.heappop(heap)[1])
            k-=1

        return ans