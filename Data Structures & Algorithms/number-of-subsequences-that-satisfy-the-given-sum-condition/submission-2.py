class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        
        nums.sort()

        MOD = 10**9 + 7
        l=0
        r=len(nums)-1
        ans = 0

        while l<=r:
            if nums[r]+nums[l] > target:
                r-=1
            else:
                ans = (ans + pow(2, r-l, MOD)) % MOD
                l+=1
        
        return ans