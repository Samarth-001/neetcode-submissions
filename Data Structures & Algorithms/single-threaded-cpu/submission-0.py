import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        primHeap = []
        secondHeap = []
        for i, task in enumerate(tasks):
            heapq.heappush(primHeap, (task[0], task[1], i))

        ans = []
        protime = 0

        while primHeap or secondHeap:
            if not secondHeap:
                protime = max(protime, primHeap[0][0])

            while primHeap and primHeap[0][0] <= protime:
                enq, time, index = heapq.heappop(primHeap)
                heapq.heappush(secondHeap, (time, index))

            time, index = heapq.heappop(secondHeap)

            ans.append(index)
            protime += time

        return ans