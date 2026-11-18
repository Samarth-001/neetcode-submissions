class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        ans = 0
        zero = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                ans = max(ans, (r-l)+1)
                continue
            
            zero+=1
            while l<=r and zero>k:
                if nums[l] == 0:
                    zero -= 1
                l+=1
            
            ans = max(ans, (r-l)+1)
                       
        return ans