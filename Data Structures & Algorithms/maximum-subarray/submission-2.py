class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum = 0
        ans = nums[0]

        for num in nums:
            
            currSum += num

            ans = max(currSum, ans)

            if currSum < 0:
                currSum = 0
        
        return ans