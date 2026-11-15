class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k == 0 or len(nums) == 0:
            return 0

        l,r = 0,0

        ans = 0
        prod = 1

        for r in range(len(nums)):
            prod = prod*nums[r]

            while l<=r and prod >= k:
                prod = prod/nums[l]
                l+=1
            
            ans+=(r-l)+1
        
        return ans