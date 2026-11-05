class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        ans = nums[0]
        sum = nums[0]

        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                sum += nums[i+1]
            else:
                sum = nums[i+1]
            
            ans = max(sum, ans)
        
        return ans