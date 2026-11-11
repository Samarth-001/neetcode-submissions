class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        l, r = 0, 0
        ans = nums[-1]

        1,2,3,3,5,6
        3
        
        while r<len(nums):
            
            if r-l>=k-1:
                ans = min(ans, (nums[r]-nums[l]))
                l+=1
            
            r+=1

        return ans