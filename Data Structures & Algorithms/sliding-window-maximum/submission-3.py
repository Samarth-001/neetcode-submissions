import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        heap = []

        l=r=0
        ans = []

        while(r<len(nums)):
            # push element
            # print("adding", -nums[r])
            heapq.heappush(heap, (-nums[r], r))
            r+=1

            # Remove the element
            if r-l+1 > k:
                while(heap[0][1] < l):
                    heapq.heappop(heap)
                l+=1
                ans.append(heap[0][0] * -1)

        # print(ans)
        return ans