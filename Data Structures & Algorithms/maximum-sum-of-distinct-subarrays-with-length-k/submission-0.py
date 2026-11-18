class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        pass

        hs = set()
        tSum,l,ans = 0,0,0
        
        for r in range(len(nums)):
            num = nums[r]
            
            if num in hs:
                while l<r and nums[l] != num:
                    tSum-=nums[l]
                    hs.remove(nums[l])
                    l+=1
                tSum-=nums[l]
                l+=1
            
            tSum+=num
            hs.add(num)
            
            if (r-l)+1 >k:
                tSum-=nums[l]
                l+=1
            if (r-l)+1 == k:
                ans = max(ans, tSum)
        
        return ans