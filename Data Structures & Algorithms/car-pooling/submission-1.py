import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        heap = []

        for passengers, fromPos, toPos in trips:
            if passengers > capacity:
                return False

            heapq.heappush(heap, (fromPos, toPos, passengers))

        heap2 = []

        currCap = 0

        while heap:
            fromPos, toPos, cap = heapq.heappop(heap)

            while heap2 and heap2[0][0] <= fromPos:
                endPos, passengers = heapq.heappop(heap2)
                currCap -= passengers

            currCap += cap

            if currCap > capacity:
                return False
            heapq.heappush(heap2, (toPos, cap))

        return True