class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefSum = 0
        hm = {0:1}
        ans = 0

        for i in range(len(nums)):
            prefSum += nums[i]

            if (prefSum-goal) in hm:
                ans+=hm[prefSum-goal]

            hm[prefSum] = hm.get(prefSum, 0)+1

        return (ans)