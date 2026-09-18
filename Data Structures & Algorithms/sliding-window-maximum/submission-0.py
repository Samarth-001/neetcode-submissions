import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        heap = []
        result = []

        for i in range(len(nums)):

            # add current element
            heapq.heappush(heap, (-nums[i], i))

            # remove elements outside window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # first window formed
            if i >= k - 1:
                result.append(-heap[0][0])

        return result