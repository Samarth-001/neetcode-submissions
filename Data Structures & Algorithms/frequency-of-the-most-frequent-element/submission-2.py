class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 1

        nums.sort()
        l, r = 0, 1
        need = 0
        ans = 0

        while r<len(nums):
            need+=(nums[r]-nums[r-1])*(r-l) 
            while need>k and l<=r:
                need -= nums[r] - nums[l]
                l+=1
            ans = max((r-l)+1,ans)
            r+=1

        return ans