import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = []

        for stone in stones:
            heapq.heappush(heap, stone*(-1))
        
        while len(heap) > 1:
            first = heapq.heappop(heap)*(-1)
            second = heapq.heappop(heap)*(-1)

            if second<first:
                heapq.heappush(heap, (first-second)*(-1))

        if len(heap)<1:
            return 0
        return heapq.heappop(heap)*(-1)