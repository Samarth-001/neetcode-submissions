class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        tsum = 0
        ans = 0
        l,r = 0, 0

        while r<len(arr):
            tsum += arr[r]

            if r-l>=k-1:
                if int((tsum)/k) >= threshold:
                    # print(l,r)
                    ans+=1
                tsum-=arr[l]
                l+=1
            r+=1
        
        return ans